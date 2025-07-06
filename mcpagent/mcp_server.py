from fastmcp import FastMCP
import openai
import google.generativeai as genai
import json
import hashlib
import os

GOOGLE_API_KEY= "<YOUR_GOOGLE_API_KEY>"
genai.configure(api_key=GOOGLE_API_KEY)
mcp = FastMCP("MCPAgent")

cache = {}
print("MCP Server is starting...")
def transcript_key(text: str) -> str:
    """Generate a unique key for the transcript based on its content."""
    return hashlib.sha256(text.encode()).hexdigest()

@mcp.tool()
def evaluate_meeting(transcript: str) -> str:
    """Evaluate the meeting transcript"""
    key = transcript_key(transcript)
    print(f"Evaluating transcript with key: {key}")
    if key in cache:
        return cache[key]
    
    try:
        
        prompt = f'''
        Transcript:
        {transcript}

        You are an AI assistant specialized in analyzing meeting transcripts. Your task is to evaluate the provided transcript and extract key insights.
        TASK: (respond in valid JSON format)

        Analyze the following meeting transcript and respond in valid JSON with these fields:

        1. summary: 3-5 bullet points summarizing the key discussion points.
        2. sentiment: overall sentiment (positive, negative, or neutral). Give brief explanation.
        3. trust_score: a score from 0 to 100 indicating the level of trust established. Give brief explanation.
        4. topics: list of financial topics discussed.
        5. action_items: list of action items with responsible parties, e.g.:
        [
            {{"description": "Follow up with the client on the proposal", "responsible_party": "Advisor"}},
            {{"description": "Prepare financial report for next meeting", "responsible_party": "Client"}}
        ]

        '''
        print(f"Generating response for transcript key: {key}")
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        content = response.text  # Gemini returns `.text`
        print(f"Received evaluation: {content}\n\n")

        if content.startswith("```json") or content.endswith("```"):
            content = content.strip("```json").strip("```").strip()
            if content.startswith("type='text' text="):
                content = content[len("type='text' text="):].strip('"')
                if content.startswith("'"):
                    content = content[1:-1]
            content = content.strip("' annotations=None")

        print(f"Processed content for evaluation: {content}")
        evaluation = json.loads(content)
        
        if not isinstance(evaluation, dict):
            raise ValueError("Response is not a valid JSON object")

        if "ERROR" in evaluation:
            raise ValueError(f"Error in evaluation: {evaluation['ERROR']}")
        
        if "summary" not in evaluation or "sentiment" not in evaluation or "topics" not in evaluation or "action_items" not in evaluation or "trust_score" not in evaluation:
            raise ValueError("Response is missing required fields: summary, sentiment, topics, action_items, trust_score")

        cache[key] = evaluation
        print(f"Evaluation for transcript key {key}: {evaluation}")
        return evaluation

    except Exception as e:
        print(f"Error evaluating transcript: {e}")
        return {"ERROR": str(e)}

if __name__ == "__main__":
    mcp.run("http")
    print("MCP Server is running...")
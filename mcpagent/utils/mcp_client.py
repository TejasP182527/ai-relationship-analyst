from fastmcp import Client
import asyncio

async def get_client():
    return Client("http://127.0.0.1:8000/mcp/")

async def analyze_transcript(transcript: str) -> dict:
    async with await get_client() as client:
        return await client.call_tool("evaluate_meeting", {"transcript": transcript})

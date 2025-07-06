import streamlit as st
from mcpagent.utils.helper import extract_client
from mcpagent.utils.data_manager import load_client_data
from mcpagent.utils.mcp_client import analyze_transcript
import asyncio

# Reset on full refresh
if "reset_done" not in st.session_state:
    st.session_state.clear()
    st.session_state["reset_done"] = True

st.set_page_config(page_title="MCP AI Agent", layout="wide")
st.title("MCPAgent")

client_list = ["Anil", "Sridhar", "Bala"]
query = st.selectbox("Select a client:", client_list)

client_name = extract_client(query)
st.markdown(f"### Analyzing insights for **{client_name.capitalize()}**")

transcript_data = load_client_data(client_name)
full_transcript = "\n".join(transcript_data.get("transcripts", []))

def run():
    with st.expander("View Transcript"):
        st.code(full_transcript[:5000] + "\n..." if len(full_transcript) > 5000 else full_transcript)

    if st.button("Run Analysis"):
        with st.spinner("Analyzing with Gemini..."):
            res = asyncio.run(analyze_transcript(full_transcript))

        print(f"Type of result: {type(res)}\n\n")
        print(f"Result: {res}\n\n")

        if isinstance(res, list) and res:
            res = res[0]
        if hasattr(res, 'text'):
            import json
            try:
                res = json.loads(res.text)
            except Exception:
                st.subheader("Summary")
                st.markdown(res.text)
                return

        st.subheader("Summary")
        summary = res.get("summary", "Not found.")
        if isinstance(summary, list):
            st.markdown("\n".join(f"- {s}" for s in summary))
        else:
            st.markdown(summary)

        st.subheader("Sentiment")
        st.markdown(res.get("sentiment", "Not detected."))
        sentiment_exp = res.get("sentiment_explanation", None)
        if sentiment_exp:
            st.caption(f"Sentiment Explanation: {sentiment_exp}")

        st.subheader("Financial Topics")
        topics = res.get("topics", [])
        for topic in topics:
            st.markdown(f"• {topic}")

        st.subheader("Action Items")
        action_items = res.get("action_items", [])
        print(f"Type of action_items: {type(action_items)}\n\n")
        for item in action_items:
            print(f"Type of item: {type(item)}\n\n")
            if isinstance(item, dict):
                desc = item.get("description", str(item))
                party = item.get("responsible_party", "") 
                st.markdown(f"- {desc} <span style='color:gray'>(Responsible: {party})</span>", unsafe_allow_html=True)
            else:
                print(f"Type of item in action_items: {type(item)}\n\n")
                st.markdown(f"- {item}")

        st.subheader("Trust Score")
        st.markdown(res.get("trust_score", "Not detected."))
        trust_exp = res.get("trust_score_explanation", None)
        if trust_exp:
            st.caption(f"Trust Score Explanation: {trust_exp}")

run()
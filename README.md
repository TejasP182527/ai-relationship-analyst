# ai-relationship-analyst

This is a **Proof of Concept (PoC)** AI-powered assistant built for Advisors, inspired by Model Context Protocol (MCP) architecture. It helps analyze client meetings and delivers contextual intelligence across:

- 🧾 Conversation Summaries  
- 😊 Sentiment Detection  
- 💡 Key Financial Topics  
- 📌 Action Items  
- 🤝 Trust Score Evaluation

The application uses **Streamlit** for a fast and intuitive UI, **Gemini2.0** for all language understanding tasks, and is structured in a modular way to mimic microservice-style agentic calls.

---

## ✨ Features

- 🧠 **Gemini-based Insights**: Extracts intelligence from meeting transcripts using Google Gemini.
- 📋 **Modular Architecture**: Each analysis task (summary, sentiment, topics) is handled in isolation.
- 📁 **JSON Transcript Storage**: Easy-to-manage and extensible client records.
- 🖥️ **Streamlit Frontend**: Minimal setup, agent-like experience.
- 🔌 **MCP-Ready**: Ready to plug into future Model Context Protocol–based infrastructure.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/TejasP182527/ai-relationship-analyst.git
cd ai-relationship-analyst
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Gemini API Key
You can get a Gemini API key at: [https://aistudio.google.com/app/apikey]

### 5. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📝 Example Transcript Format

```json
{
  "name": "Client1",
  "transcripts": [
    "Hi Client1, as an NRI based in Singapore, your portfolio is showing consistent returns. However, there's an increasing TDS deduction on your Indian dividend income. I suggest routing dividends into a reinvestment plan or transferring part of your holdings into offshore mutual funds...",
    "We also discussed optimizing the USD-INR hedge. Currently, you're overexposed to rupee volatility..."
  ]
}
```

## 🔮 Powered By

- [Streamlit](https://streamlit.io/) – Interactive frontend
- [Google Gemini](https://ai.google.dev/) – LLM-backed intelligence


## 📜 License
This PoC is designed for **Research purpose only** 
Not licensed for public distribution or production deployment.

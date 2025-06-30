# BlogAgentic: End-to-End Blog Generator with LangGraph and Groq LLM

![LangGraph](https://img.shields.io/badge/LangGraph-Graph%20AI-green)
![Groq LLM](https://img.shields.io/badge/Groq-LLM-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)

---

## Overview

**BlogAgentic** is a Python-based, end-to-end blog generation service that:

✅ Generates creative blog titles based on user-supplied topics  
✅ Produces detailed blog content in Markdown  
✅ Translates the blog into multiple languages (e.g. Urdu, French)  
✅ Uses LangGraph to orchestrate tasks as a state machine graph  
✅ Serves as an API with FastAPI for easy integration

Built on top of **LangGraph**, **Groq LLM**, and **LangChain** for fast, scalable AI content generation.

---
## Demo / Screenshots

### Langgraph Interface  
![Langsmith Interface](https://github.com/iqrai1/blogagentic_end_to_end_langgraph/blob/main/assets/langgraph_studio.png)
### Postman FastAPI Interface 
![Postman Architecture](https://github.com/iqrai1/blogagentic_end_to_end_langgraph/blob/main/assets/Postman_api.png)

---

## Installation

```bash
# 1. Clone the Repository
git clone https://github.com/iqrai1/blogagentic_end_to_end_langgraph.git
cd blogagentic_end_to_end_langgraph

# 2. Create a Virtual Environment
python -m venv .venv
.venv\Scripts\activate  # (Windows)
# source .venv/bin/activate  # (macOS/Linux)

# Set Environment Variables (in your .env file or shell)
# GROQ_API_KEY=your_groq_api_key
# LANGCHAIN_API_KEY=your_langchain_api_key

# Running the Application
uvicorn app:app --reload
# Visit http://127.0.0.1:8000

# API Endpoint Example:
# POST /blogs
# {
#     "topic": "Ethics of Artificial Intelligence",
#     "language": "french"
# }

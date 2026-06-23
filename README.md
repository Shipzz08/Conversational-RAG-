# Conversational RAG System

A robust **Conversational Retrieval-Augmented Generation (RAG)** system that enables users to query PDFs and YouTube transcripts through an intelligent chat interface. Built with Python, LangChain and ChromaDB, the system provides grounded, context-aware answers while maintaining conversation history.

---

## 🚀 Features

- **Multi-Source Ingestion:**
  - **PDF Documents:** Upload and index local PDF files.
  - **YouTube Transcripts:** Fetch and process transcripts from any YouTube URL.
- **Advanced RAG Pipeline:**
  - **Semantic Chunking:** Splits documents into meaningful segments.
  - **Vector Search:** Uses ChromaDB for efficient similarity retrieval.
  - **Contextual Memory:** Maintains chat history to handle follow-up questions accurately.
- **Multi-Provider Support:**
  - **LLMs:** OpenAI (GPT-3.5/4), Anthropic (Claude 3), and NVIDIA NIM (Llama 3).
  - **Embeddings:** OpenAI, NVIDIA, or local HuggingFace models.
- **Source Transparency:** View the exact excerpts and sources used to generate each response.
- **Interactive UI:** A clean, Streamlit-based interface for seamless user interaction.

---

## 🏗️ Project Structure

```text
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
├── .env.example            # Template for environment variables
├── src/
│   ├── ingestion/          # PDF and YouTube loading logic
│   ├── processing/         # Text cleaning and chunking
│   ├── retrieval/          # Vector store management (ChromaDB)
│   ├── chains/             # RAG orchestration and prompt logic
│   └── ui/                 # Streamlit interface
└── tests/                  # Unit tests for core components
```

---

## 🛠️ Technical Stack

- **Framework:** [LangChain](https://github.com/langchain-ai/langchain)
- **Vector Database:** [ChromaDB](https://www.trychroma.com/)
- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Providers:** OpenAI, Anthropic, NVIDIA
- **Embeddings:** OpenAI, NVIDIA, HuggingFace
- **Testing:** Pytest

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd conversational-rag
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Configuration

1. Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```

2. Configure your API keys and preferred providers in `.env`:
   ```env
   # API Keys
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=...
   NVIDIA_API_KEY=...

   # Provider Selection (openai, anthropic, nvidia)
   LLM_PROVIDER=openai
   EMBEDDING_PROVIDER=openai

   # Model Selection
   OPENAI_MODEL=gpt-3.5-turbo
   ANTHROPIC_MODEL=claude-3-sonnet-20240229
   NVIDIA_MODEL=meta/llama3-70b-instruct
   EMBEDDING_MODEL=text-embedding-3-small
   ```

---

## 🏃 Usage

1. **Start the application:**
   ```bash
   python main.py
   ```
   *This will launch the Streamlit server, typically at `http://localhost:8501`.*

2. **Ingest Content:**
   - Use the sidebar to upload a **PDF** or enter a **YouTube URL**.
   - Click **"Process"** to index the content into the vector store.

3. **Start Chatting:**
   - Ask questions in the chat input.
   - Use follow-up questions (e.g., "Can you explain that more simply?").
   - Expand the **"View Sources"** section to see retrieved context.

---

## 🧪 Testing

Run the test suite using `pytest`:
```bash
pytest
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

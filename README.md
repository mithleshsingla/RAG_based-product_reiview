This is a product recommendation system based on RAG artitecture.
```
┌────────────┐
│ User Input │ ◄─── ("what about battery life?")
└─────┬──────┘
      │
      ▼
────────────────────────────────────────────────────
        📦 RunnableWithMessageHistory
────────────────────────────────────────────────────
      │
      ▼
🧠 get_session_history(session_id)
┌────────────────────────────────────┐
│ Fetch or create per-user chat log │
└────────────────────────────────────┘
      │
      ▼
────────────────────────────────────────────────────
    🧠 create_history_aware_retriever()
────────────────────────────────────────────────────
      │
      │ Reformulate input using model + history:
      │   ➤ "What is the battery life of the best bluetooth buds?"
      ▼
  🔍 Retriever.as_retriever(k=3)
┌────────────────────────────────────┐
│ Search vector DB (Astra) for top 3 │
│ matching product reviews/titles    │
└────────────────────────────────────┘
      │
      ▼
────────────────────────────────────────────────────
      create_stuff_documents_chain()
────────────────────────────────────────────────────
      │
      ▼
📝 Prompt Template:
  - Injects `context` from retrieved docs
  - Injects user `input` (reformulated)
  - Adds system instructions
      │
      ▼
🤖 Ollama / LLM (qwen2.5:0.5b)
  - Generates concise, product-aware response
      │
      ▼
🧾 Output
"These buds offer up to 30 hours of battery life..."

────────────────────────────────────────────────────
📜 Memory:
Stores user input, context, and model response
for session ID "mithlesh"
────────────────────────────────────────────────────
```

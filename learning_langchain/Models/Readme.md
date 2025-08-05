# Models

The **Model Component** in LangChain is a crucial part of the framework, designed to facilitate interactions with various language models and embedding models.

It abstracts the complexity of working directly with different LLMs, chat models, and embedding models, providing a uniform interface to communicate with them. This makes it easier to build applications that rely on AI-generated text, text embeddings for similarity search, and retrieval-augmented generation (RAG).

---

### Models Overview

```

Models: Language Models     |   Embedding Models
        |
        V
LLMs    |  Chat Models

```

- **Language Models:** `text(input)` → `text(output)`
- **Embedding Models:** `text(input)` → `embedding(output)`

---

## Language Models

Language Models are AI systems designed to process, generate, and understand natural language text.

### Types of Language Models

- **LLMs (Large Language Models):**  
  General-purpose models used for raw text generation.  
  Input: Plain text → Output: Plain text  
  These are traditionally older models and are not widely used now.

- **Chat Models:**  
  Language models specialized for conversational tasks.  
  Input: Sequence of messages → Output: Chat message(s)  
  These are newer and more commonly used than LLMs.

> **Note:** LLMs are becoming deprecated in favor of Chat Models which are more context-aware and structured.

---

### Comparison Table

| Feature              | LLMs (Base Models)                              | Chat Models (Instruction-tuned)                              |
|----------------------|--------------------------------------------------|---------------------------------------------------------------|
| **Purpose**          | Free-form text generation                        | Optimized for multi-turn conversations                        |
| **Training Data**    | General text corpora (books, articles)           | Fine-tuned on chat datasets (dialogues, user-assistant chats) |
| **Memory & Context** | No built-in memory                               | Support structured conversation history                       |
| **Role Awareness**   | No concept of "user" or "assistant" roles        | Understands "system", "user", and "assistant" roles           |
| **Example Models**   | GPT-3, LLaMA-2-7B, Mistral-7B, OPT-1.3B          | GPT-4, GPT-3.5-turbo, LLaMA-2-Chat, Mistral-Instruct, Claude  |
| **Use Cases**        | Text generation, summarization, translation, creative writing, code generation | Conversational AI, chatbots, virtual assistants, customer support, AI tutors |

---


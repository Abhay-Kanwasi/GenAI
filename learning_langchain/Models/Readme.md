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
  
    `temperature` is a parameter that controls the randomness of a language model's output. It affects how creative or deterministic the response are:
      - lower values (0.0 - 0.3) -> More deterministic, and predictable
        - higher values (0.7 - 1.5) -> More random, creative and diverse.
        
    | Use Case                                      | Recommended Temperature 
    |-----------------------------------------------|-------------------------|
    | Factual answers(math, code, facts)            | 0.0 - 0.3               |
    | Balanced response(general QA, explanations)   | 0.5 - 0.7               |
    | Creative writing, storytelling, jokes         | 0.9 - 1.2               |
    | Maximum Randomness(wild ideas, brainstorming) | 0.5+                    |
    
    `max_completion_tokens` is for restricting the output from ChatModel.
    
    - Close Source Models : These models are paid models which are maintained by their organization. Example: google-gemini-api(Google), claude-api(Anthropic)
    - Open-source Models : Open source language models are freely available AI models that can be downloaded, modified, fine-tuned and deployed without restrictions from a central provider. Unlike closed-source model such as OpenAI's GPT-4, Anthropic Claude or Google Gemini, open-source models allow full control and customization. 
      Where to find them ? : HuggingFace is the largest repository of open-source LLMs
      Ways to use Open-source models: Using HF Interface API or Run Locally
      Disadvantages:
      - High Hardware Requirements:  Running large models (e.g., LLaMA-2-70B) requires expensive GPU.
      - Setup Complexity: Requires installation of dependencies like PyTorch, CUDA, transformers.
      - Lack of RLHF: Most open-source models don't have fine-tuning with human feedback making them weaker in instruction-following.
      - Limited Multimodal Abilities: Open model don't support images, audio or video like GPT-4V.
  
   | Feature          | Open-Source Models                              | Closed-Source Models                   |
   |------------------|-------------------------------------------------|----------------------------------------|
   | **Purpose**      | Free-form text generation                       | Optimized for multi-turn conversations |
   | **Control**      | Can modify, fine-tuned and deployed anywhere    | Locked to provider's infrastructure    |
   | **Data Privacy** | Runs locally (no data sent to external servers) | Sends queries to provider's servers    |
   | **Customization** | Can fine-tune on specific datasets              | No access to fine-tuning in most cases |
   | **Deployment**   | Can be deployed on on-premise servers or cloud  | Must use vendor's API                  |

 
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


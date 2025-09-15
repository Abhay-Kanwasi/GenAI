# Runnables

Runnables in LangChain provide a structured and modular way to define, execute, and manage tasks within a pipeline. They encapsulate various components such as models, tools, chains, and custom logic, making them reusable and composable. This feature is particularly useful for building complex workflows, as it allows developers to break down tasks into smaller, manageable units.

A Runnable is a building block that represents a single task or operation. Tasks can include running a language model, processing data, or chaining multiple operations together.Multiple Runnables can be linked together to form a pipeline.Runnables support asynchronous execution, enabling faster and more efficient task management, especially in workflows involving I/O-bound operations.

Runnables integrate seamlessly with LangChain’s ecosystem of tools, models, chains, and utilities.

Now that we've explored how Runnables allow us to compose complex LLM pipelines using simple, reusable components, let's examine how they interact with external data sources.

A typical LLM can generate fluent text, but without access to up-to-date or private knowledge, its usefulness becomes limited in real-world applications. This is where the Retriever comes into play.

### Retriever
In LangChain, a Retriever is a component designed to fetch relevant information — such as documents, paragraphs, or data chunks — in response to a user query. Much like an LLMChain is a Runnable, a Retriever is also a runnable-compatible building block that can be inserted seamlessly into your pipeline.

Imagine a chatbot that needs to answer questions about your internal documentation. A RunnableSequence might first pass the user’s question to a Retriever, which returns the top relevant chunks, and then forward those to the LLM for generating a grounded response.

#### Simple RAG Flow

```text
User Query
   │
   ▼
[Embedding Model]
   │
   ▼
[Vector Database Search]
   │
   ▼
[Relevant Documents Retrieved]
   │
   ▼
[Prompt Template Filled with Context]
   │
   ▼
[LLM Generates Response]
   │
   ▼
Final Answer to User
```


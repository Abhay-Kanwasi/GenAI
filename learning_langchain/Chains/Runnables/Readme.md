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

I have created two files how Runnables are needed in langchain and how they standardized the whole process and cut the learning curve. 

- `WithoutRunnableDummyLangchain`: In this file what you will see is that how without runnable all the langchain components such as are being used together but don't have any common interface. I have created some dummy code examples for how things will be working in original langchain.
- `WithRunnableDummyLangchain`: In this file we are creating components using Abstract methods thus standardizing the whole code.


## Types of Runnables

1. Task Specific Runnables
These are core Langchain Components that have been converted into Runnables so they can be used in pipelines. Their purpose to perform task-specific operations like LLM calls, prompting, reterival etc. RunnableSequence is a sequential chain of runnables in Langchain that executes each step one after another, passing the output of one step as the input to the next.
It is useful when you need to compose multiple runnables togehter in structured workflow
`Examples:` 
- ChatOpenAI : Runs an LLM model.
- PromptTemplate : Formats prompts dynamially.
- Retriver : Retrieves relevant documents.

2. Runnables Primitive
These are fundamental building blocks for structuring execution logic in AI workflows. Their purpose is that they help orchestrate execution by defending how different Runnables interact(sequentially, in parllel, conditionally. etc)
`Examples:`
- RunnableSequence : Runs steps in order (`|` operator)
- RunnableParllel : Runs multiple steps simultaneously. 
- RunnableMap : Maps the same input across multiple functions.
- RunnableBranch : Implements conditional execution (if-else logic).
- RunnableLambda : Wraps custom Python functions into Runnables.
- RunnablePassthrough : Just forwards input as output (acts as a placeholder).



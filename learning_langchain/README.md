# LangChain

LangChain is an open-source framework for developing applications powered by Large Language Models (LLMs). It provides modular components and abstractions that simplify the process of building robust, intelligent systems using LLMs.

---

### Why do we need LangChain?

LLMs are powerful, but using them in real-world applications requires more than just sending prompts and receiving responses. You need to handle things like memory, multi-step reasoning, tool usage, and integration with data sources. LangChain makes this easier by offering:

- **Composable Components**: Like chains(one output automatically become second input), agents, memory, and tools that can be connected together to build complex flows.
- **Abstractions**: Simplifies prompt engineering, output parsing, and model usage.
- **Integration**: Easily connects LLMs with APIs, vector stores, documents, and external tools.
- **State & Memory**: Enables persistent context across interactions.

LangChain helps developers go from LLM toy demos to production-ready apps with minimal effort.

---

### Benefits

- **Concepts of Chains**: Build multi-step pipelines (input → LLM → post-process).
- **Model Agnostic Development**: Use OpenAI, Anthropic, Hugging Face, or custom models.
- **Complete Ecosystem**: Includes integrations with vector databases, tools, web APIs, and more.
- **Memory and State Handling**: Keep conversational or task history with support for both ephemeral and persistent memory.
- **Tool Use & Agents**: Empower LLMs to call functions, access tools, or search documents autonomously.

---

### What can you build?

- Conversational Chatbots with memory and tool-use
- AI Knowledge Assistants that retrieve from custom data
- Autonomous AI Agents that reason and act
- Workflow Automation pipelines powered by LLMs
- Summarization and Research Tools

---

## Main Components

LangChain is built around modular components that make it easy to interact with large language models (LLMs) and build powerful applications. Here are some of the most important ones:

---

### Models

In LangChain, **models** are the core interfaces through which you interact with AI services. Different model providers (e.g., OpenAI, Anthropic, Cohere) have their own API formats, which can become cumbersome when switching or using multiple providers.

LangChain solves this by providing a **standardized interface** to communicate with different models using the same code structure.

There are **two primary types of models**:

1. **Language Models (LLMs)**  
   - **Workflow**: `input (text) → LLM → output (text)`  
   - **Use Case**: Chatbots, summarization, question-answering, etc.

2. **Embedding Models**  
   - **Workflow**: `input (text) → LLM → output (vectors)`  
   - **Use Case**: Semantic search, document similarity, retrieval-based systems

---

### Prompts

**Prompts** are the instructions or questions sent to LLMs to generate responses. LangChain provides a flexible way to create prompts that are dynamic, reusable, and structured.

---

##### Dynamic and Reusable Prompts

Use `PromptTemplate` to create reusable templates with placeholders:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template('Summarize {topic} in {emotion} tone.')
print(prompt.format(topic='cricket', emotion='fun'))
````

> Output: `Summarize cricket in fun tone.`

---

##### Role-Based Prompts

Use structured role messages (system, user, assistant) to better control behavior:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
   ("system", "Hi you are an experienced {profession}"),
   ("user", "Tell me about {topic}")
])

formatted_message = chat_prompt.format_messages(
    profession="Doctor", topic="Viral Fever"
)
```

> Output: `[SystemMessage(content='Hi you are an experienced Doctor'),
 UserMessage(content='Tell me about Viral Fever')]`

---

##### Few-Shot Prompting

Include multiple examples in the prompt to guide the LLM toward better performance on specific tasks.

```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
   
# Step 1
examples = [
   {"input": "I was changed twice for my subscription this month.", "output": "Billing Issue"},
   {"input": "The app crashes every time I try to log in.", "output": "Technical Problem"},
   {"input": "Can you explain how to upgrade my plan?", "output": "General Inquiry"},
   {"input": "I need a refund for a  payment I didn't authorize.", "output": "Billing Issue"}
]

# Step 2 : Create an example templates
example_template = """
Ticket: {input}
Category: {output}
"""

# Step 3: Build the few-shot prompt template
few_shot_prompt = FewShotPromptTemplate(
   examples=examples, 
   example_prompt=PromptTemplate(input_variables=["input", "output"], template=example_template),
   prefix="Classify the following customer support tickets into one of the categories: 'Billing Issues', 'Technical Problem', 'General Inquiry'.\n\n",
   suffix="\nTicket: {user_input}\nCategory:",
   input_variables=["user_input"],
)
```
Output:
```text
Classify the following customer support tickets into one of the categories:
'Billing Issues', 'Technical Problem', 'General Inquiry'.

Ticket:  I was charged twice for my subscription this month.  
Category: Billing Issue

Ticket:  The app crashes every time I try to log in.  
Category: Technical Problem

Ticket:  Can you explain how to upgrade my plan?  
Category: General Inquiry

Ticket:  I need a refund for a payment I didn't authorize.  
Category: Billing Issue

Ticket:  I am unable to connect to the internet using your service.  
Category: 
```
---

### Chains

**Chains** in LangChain help you build **multistep LLM pipelines**. They allow you to connect different components — such as prompts, LLMs, tools, and output parsers — so that the **output of one step becomes the input of the next**.

This enables you to move beyond single-prompt queries and build more advanced workflows like summarization pipelines, chat agents, or data processors.

---

##### Basic LLMChain

The most common chain is `LLMChain`, which combines a prompt and an LLM into a single callable object.

##### Example:

```python
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

# Create a prompt template
prompt = PromptTemplate.from_template("Write a short poem about {topic}")

# Initialize the LLM (e.g., OpenAI)
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create the chain
chain = LLMChain(prompt=prompt, llm=llm)

# Run the chain
response = chain.invoke({"topic": "sunsets"})
print(response)
```

Output:
```text
A golden glow, the sky ignites,  
As day gives way to dreamy nights.  
The sun sinks low, the colors spread,  
In hues of orange, gold, and red.
```

---

##### Chaining Multiple Steps

You can combine multiple chains using `SimpleSequentialChain` or `SequentialChain` to create multi-step logic.

##### Example: Generate → Summarize

```python
from langchain.chains import SimpleSequentialChain
from langchain_core.prompts import PromptTemplate

# Step 1: Generate content
generate_prompt = PromptTemplate.from_template("Write a paragraph about {topic}")
generate_chain = LLMChain(llm=llm, prompt=generate_prompt)

# Step 2: Summarize it
summarize_prompt = PromptTemplate.from_template("Summarize the following: {input}")
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

# Combine chains
overall_chain = SimpleSequentialChain(chains=[generate_chain, summarize_chain])

# Run it
response = overall_chain.invoke({"topic": "rainforests"})
print(response)
```

Output:

```text
Rainforests are lush, biodiverse ecosystems found in tropical regions...
```

---

Chains make it easy to **compose logic**, **reuse prompts**, and **scale workflows** — making your LLM applications more maintainable and powerful.

---

### Indexes

**Indexes** connect your application to external knowledge — such as PDFs, websites, or databases — allowing language models to access relevant information beyond their training data.

LangChain handles this through four main components:

- **Document Loader** – Loads data from external sources like PDFs or web pages.
- **Text Splitter** – Breaks large documents into smaller chunks to fit within LLM token limits.
- **Vector Store** – Stores embeddings (numerical representations) of chunks for fast similarity search.
- **Retriever** – Finds the most relevant chunks for a user's query using vector similarity.

---

#### Example Workflow: Chat with a PDF

Imagine you want to let users ask questions about a PDF (e.g., a legal contract or user manual). Here's how the process works:

1. **Upload PDF**  
   The user uploads a PDF file to cloud storage (e.g., an S3 bucket).

2. **Document Loading**  
   A **document loader** reads the content from the PDF file — extracting raw text from each page.

3. **Text Splitting**  
   The text is often too long for an LLM to process at once.  
   A **text splitter** breaks the content into smaller, overlapping chunks — preserving context.

4. **Embedding & Indexing**  
   Each chunk is passed through an **embedding model** to convert it into a vector (a numeric representation of its meaning).  
   These vectors are stored in a **vector database** (like FAISS, Pinecone, or Chroma).

5. **Retrieval on User Query**  
   When the user asks a question:
   - The question is converted into a vector using the same embedding model.
   - This query vector is compared against the stored vectors in the vector DB using **semantic search**.
   - The most relevant chunks (based on vector similarity) are retrieved.

6. **Response Generation**  
   The retrieved chunks + the user's original query are passed to the LLM.  
   The LLM then returns a **concise, context-aware answer**.

This approach enables the LLM to answer questions grounded in your own documents — even though it was never trained on them.

---

### Memory
LLM api calls are stateless.
In traditional LLM interactions, each input is treated independently — meaning the model forgets everything after every prompt.  
**Memory** in LangChain solves this by allowing your application to **retain context between interactions**, enabling more natural, conversational, and personalized experiences.

LangChain provides different types of memory for different use cases:

---

#### Why Memory is Important

Without memory:

- The user must repeat context in every message.
- The model can't keep track of ongoing conversations or tasks.
- Chatbots feel robotic and unaware of past messages.

With memory:

- The LLM can remember past questions and answers.
- Conversations feel more fluid and human-like.
- You can build assistants that evolve over time — like remembering user preferences or past actions.

---

#### Types of Memory

1. **Conversation Buffer Memory**  
   Stores a simple list of messages in memory (short-term chat history).  
   Best for short, linear conversations.

2. **ConversationBufferWindowMemory**

   Only keeps the last N interactions to avoid excessive token usage.

3. **Summary Memory**  
   Instead of storing the entire history, it stores a **summarized version** of past messages.  
   Useful when token limits are tight but long-term context is needed.

4. **Vector Store Memory**  
   Stores past interactions as **embeddings**, allowing retrieval of relevant past messages using semantic similarity.

5. **Custom Memory**
   For advanced use cases, you can store specialized state(e.g., the user's prefers or key facts about them) in a custom memory class.
---

#### Example Use Case: Personalized Chatbot

Let’s say a user starts a conversation with your AI assistant:

- **User**: “Hi, my name is Arjun.”
- **User**: “Can you remind me to call my dentist tomorrow?”
- **User**: “Also, book me a cab for 10 AM.”

With **memory** enabled:

- The bot knows your name is Arjun in future messages.
- It can reference tasks or preferences mentioned earlier.
- It can personalize answers:  
  > “Hi Arjun, just a reminder to call your dentist today. Also, your cab is booked for 10 AM.”

---

Memory transforms a one-shot LLM into a **stateful assistant** — making your application feel smarter, more human, and more useful over time.

---

### AI Agents

**Agents** are one of the most powerful features in LangChain.  
While a basic chain runs a fixed set of steps, **agents can make decisions on-the-fly** about what tools to use and in what order — just like a human would.

---

#### What is an Agent?

An agent uses a language model as a **reasoning engine** to:
- Understand a user's request
- Decide what actions (or tools) are needed to fulfill it
- Use those tools dynamically
- Combine results and generate a final answer

It’s like giving your LLM **a brain (reasoning)** and **hands (tools)**.

---

#### What Tools Can Agents Use?

LangChain allows you to give agents access to:
- Web search
- Python REPL (code execution)
- Calculators
- Databases
- APIs (like weather, news, etc.)
- Your own custom functions

---

#### Example Workflow: AI Personal Assistant

Let’s say the user asks:

> "What’s the weather in Delhi today, and schedule a meeting if it’s sunny?"

Here’s how the agent would handle it:

1. **Understand the task**: There are two parts — check weather and possibly schedule a meeting.
2. **Tool use #1**: Call a weather API tool to get today’s forecast.
3. **Decision-making**: If the forecast is sunny, proceed to next step.
4. **Tool use #2**: Call a calendar scheduling API to create the meeting.
5. **Respond**: Summarize what was done and show the user confirmation.

---

#### Agents vs Chains

| Feature       | Chains                        | Agents                             |
|---------------|-------------------------------|-------------------------------------|
| Workflow      | Fixed sequence of steps       | Dynamic, tool-based decision-making |
| Flexibility   | Limited to hardcoded logic    | Flexible, adapts at runtime         |
| Use Cases     | Summarization, Q&A, chatbots  | Assistants, automation, reasoning   |

---

Agents are best used when:
- The task involves multiple tools or data sources
- You don’t know ahead of time which tools will be needed
- You want autonomous, intelligent behavior from your app

With agents, you can build LLM apps that can **think, plan, and act** — like digital coworkers or smart assistants.


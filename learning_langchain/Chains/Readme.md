# Chains 

A **chain** is a way to connect multiple steps together into a single pipeline.  
Instead of calling each step manually, you link them so the data flows automatically.  

---

#### Without a Chain (Manual Steps)

You handle each step one by one:

1. **Fill the template** with input values → produces a prompt.  
2. **Send the prompt** to the model → produces a result.  

```python
prompt = template.invoke({"paper": "GPT-3"})
result = model.invoke(prompt)
````

---

#### With a Chain (Automatic Pipeline)

You connect the template **directly** to the model.
Now you can pass the inputs once, and the chain takes care of everything.

```python
chain = template | model
result = chain.invoke({"paper": "GPT-3"})
```

### Behind the Scenes

```
(your inputs) → [template] → [model] → [result]
```

---

#### Analogy

* **Manual Way** → Cooking step by step (chop → cook → serve).
* **Chain** → Kitchen machine (put ingredients in, it chops + cooks + serves).

---

#### When to Use

**Chains** → When you want fewer lines of code and automatic flow.
**Manual steps** → When you want more control and easier debugging.

---

#### Visualize the chain 
We can visualize our chain pipeline using `chain.get_graph().print_ascii()`

## Types of Chains 

LangChain offers various types of **chains** to help developers build AI workflows. A **chain** is simply a pipeline that connects components like LLMs, retrievers, and prompt templates to perform complex tasks such as question answering, summarization, or data extraction.

---

##### Why Are There So Many Chains?

LangChain introduced many chains over time, and while this was meant to support a wide range of use cases, it also introduced some challenges:

* The codebase became more complex.
* Developers had to learn and understand many specialized chains.
* It became harder to maintain and scale applications.

These chains were created not only to solve different problems but also to help developers stitch together components that were originally **not standardized** in how they interact with each other.

---

##### Why Standardization Was an Issue

A major reason for the proliferation of chains was the **lack of a common interface** among core LangChain components. Each component had its own method of interaction:

| Component        | Interaction Method         |
| ---------------- | -------------------------- |
| `LLM`            | `predict()`                |
| `PromptTemplate` | `format()`                 |
| `Retriever`      | `get_relevant_documents()` |

Since these components were designed to serve different purposes and were developed independently, they did not follow a unified pattern. As a result, developers needed to write **custom code** to connect these components in a meaningful way.

To handle this, LangChain introduced custom chains like `LLMChain`, `RetrievalQA`, and others—each tailored to specific workflows.

---

##### Not Just Standardization: Workflow Abstractions

It’s important to note that these chains were not created **only** because of non-standard components. Many of them were designed to encapsulate **common patterns** in language model workflows. For example:

* `RetrievalQA` handles document retrieval and question answering.
* `MapReduceDocumentsChain` handles summarization by processing documents in a map-reduce style.

So while the lack of standard interfaces was one reason for many chains, another reason was to **abstract common use cases** into reusable templates.

---

##### The Solution: Runnable Interface

To address these issues, LangChain introduced the **`Runnable` interface**.

This interface standardizes how components are invoked, regardless of what they do. Every component that implements `Runnable` can be used interchangeably in a pipeline with a consistent method:

```python
output = component.invoke(input)
```

Benefits of `Runnable`:

* A unified way to call different components.
* Easier composition and chaining of modules.
* Reduces the need for use-case-specific chains.

This shift allows developers to create custom chains more easily, using basic building blocks that all behave consistently.

---

##### Common Chains in LangChain (with Descriptions)

| Chain Name                     | Description                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `LLMChain`                     | Basic chain that takes a prompt, formats it, and sends it to an LLM.                |
| `RetrievalQA`                  | Retrieves relevant documents and feeds them to an LLM for answering a query.        |
| `ConversationalRetrievalChain` | Adds chat history for contextual question answering.                                |
| `StuffDocumentsChain`          | Combines all documents into a single input prompt for the LLM.                      |
| `MapReduceDocumentsChain`      | Applies the LLM to each document individually, then combines the results.           |
| `RefineDocumentsChain`         | Iteratively builds an answer by refining it with each new document.                 |
| `SimpleSequentialChain`        | Runs multiple chains in a strict sequence; output of one becomes input to the next. |
| `SequentialChain`              | More flexible than `SimpleSequentialChain`; allows passing data across steps.       |

---

LangChain initially introduced many chains to handle various workflows and bridge gaps between non-standard components. However, this led to complexity and a steeper learning curve.

To solve this, LangChain introduced the `Runnable` interface, which provides a standardized way to compose and invoke components. They all follow the same interface. As a result, developers can now build their own chains more flexibly, without relying on a large set of predefined ones.

This marks a shift from a "many-chains" approach to a **modular, composable system**, making AI application development simpler and more maintainable.

Absolutely — here's a more **conversational and human-friendly version** of your explanation, keeping it informative but easy to follow. It's still in Markdown, so you can use it for documentation, blogs, or internal notes.

---

## Building Workflows with Runnables: Think Like Lego

In LangChain, every component that does something useful — like formatting prompts, calling an LLM, or retrieving documents — can be turned into a **Runnable**. The beauty of this system is that you can connect these components **together** to build powerful AI workflows.

Let’s break this down.

---

### What Happens When You Connect Runnables?

Imagine you have two Runnables:

* `R1`: formats a prompt
* `R2`: sends that prompt to an LLM

You can connect them like this:

```python
workflow = R1 | R2
```

That’s it. The output of `R1` becomes the input for `R2`, automatically. You don’t have to manually pass values between them — LangChain takes care of that.

And here’s the really cool part: **this whole thing (`workflow`) is also a Runnable**. You can treat it just like any other component.

```python
result = workflow.invoke({"topic": "developer"})
```

This makes everything feel very modular and reusable.

---

### Think of Runnables Like Lego Blocks

A great way to understand how this works is to think of **Lego blocks**:

* **Each block has its own purpose** — some are small, some are large, some have special functions.
* But **every block follows the same connection system** — those little studs and holes.
* You can connect 3 or 4 blocks to build something more useful — maybe a car, or a spaceship.
* That larger thing? You can treat it as a single unit and plug it into something even bigger.

LangChain Runnables work the same way.

> You have small, focused components. You connect them together using a common interface. And suddenly, you're building complex workflows from simple parts.

---

### Why This Matters

This model gives you a few big advantages:

* **Reusability**: You can build a small piece once and reuse it everywhere.
* **Simplicity**: No need for boilerplate glue code to connect different components.
* **Flexibility**: You’re not locked into one “chain” or flow — you can remix things however you like.
* **Scalability**: You can take small workflows and plug them into even bigger ones.

---

### A Simple Example

Here’s what it looks like in practice:

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# A prompt that accepts a topic
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")

# A language model
llm = ChatOpenAI()

# Combine them into a workflow
workflow = prompt | llm

# Use the workflow like any other runnable
response = workflow.invoke({"topic": "startups"})
print(response)
```

You didn’t have to worry about calling `.format()` or `.predict()` — everything just worked because both `prompt` and `llm` follow the `Runnable` interface.

LangChain's move toward `Runnable` is all about **making things composable and predictable**.

Just like Lego blocks:

* You can use simple pieces to build complex systems.
* Every piece knows how to connect to the next.
* And once you’ve built something, you can plug it into even more creative workflows.

No custom chains. No messy glue code. Just clean, flexible building blocks.

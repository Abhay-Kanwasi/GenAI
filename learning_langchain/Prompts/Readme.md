# Prompts

Prompts are the input instructions or queries given to a model to guide its output.

---

## Types of Prompts
- **Text-based**
- **Multimodal** (image / sound / video)

---

## Static vs Dynamic Prompts
- **Static Prompts** – Fixed text that never changes.
- **Dynamic Prompts** – Generated or modified at runtime, often using variables or data from user input.

---

## Prompt Template

A **PromptTemplate** in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template.  
Instead of hardcoding prompts, `PromptTemplate` allows you to define **placeholders** that can be filled at runtime with different values.

### Benefits
- **Reusable**
- **Flexible**
- **Easy to manage**, especially when working with dynamic user inputs or automated workflows.

---

### Why use `PromptTemplate` over f-strings?
1. **Default validation** – Ensures required variables are provided.
```python
from langchain_core.prompts import PromptTemplate
PromptTemplate(
   template="<prompt>",
   input_variables=["input-variable"],
   validate_template=True
)
```

2. **Reusability** – Easily reuse prompt structures in different contexts.
3. **LangChain ecosystem compatibility** – Integrates smoothly with LangChain tools and chains.

---

## Diagram (Text-based)

```
invoke()
   |
   +-- single_message  (single-turn stand-alone queries)
   |        |
   |        +-- Static Message
   |        +-- Dynamic Message
   |
   +-- list_of_messages  (multi-turn conversation)
            |
            +-- Static Message
            |       - System Message
            |       - Human Message
            |       - AI Message
            |
            +-- Dynamic Message
```

---

## Messages

* **System Message** – Message for priming AI behavior. Usually passed as the first of a sequence of input messages.
* **Human Message** – Message from a human. Passed from the user to the model.
* **AI Message** – Message from an AI. Returned from a chat model as a response to a prompt.
  This message contains:

  * The raw output from the model.
  * Standardized fields (e.g., tool calls, usage metadata) added by LangChain.

---

## Message Placeholder

A **Message Placeholder** in LangChain is a special placeholder used inside a `ChatPromptTemplate` to dynamically insert chat history or a list of messages at runtime.

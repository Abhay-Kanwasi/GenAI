# Prompts

Prompts are the input instructions or queries given to a model to guide its output.

---

#### Types of Prompts
- **Text-based**
- **Multimodal** (image / sound / video)

---

#### Static vs Dynamic Prompts
- **Static Prompts** – Fixed text that never changes.
- **Dynamic Prompts** – Generated or modified at runtime, often using variables or data from user input.

---

#### Prompt Template

A **PromptTemplate** in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template.  
Instead of hardcoding prompts, `PromptTemplate` allows you to define **placeholders** that can be filled at runtime with different values.

#### Benefits
- **Reusable**
- **Flexible**
- **Easy to manage**, especially when working with dynamic user inputs or automated workflows.

---

#### Why use `PromptTemplate` over f-strings?
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

#### Diagram (Text-based)

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

#### Messages

* **System Message** – Message for priming AI behavior. Usually passed as the first of a sequence of input messages.
* **Human Message** – Message from a human. Passed from the user to the model.
* **AI Message** – Message from an AI. Returned from a chat model as a response to a prompt.
  This message contains:

  * The raw output from the model.
  * Standardized fields (e.g., tool calls, usage metadata) added by LangChain.

---

#### Message Placeholder

A **Message Placeholder** in LangChain is a special placeholder used inside a `ChatPromptTemplate` to dynamically insert chat history or a list of messages at runtime.


#### Structure Output
In langchain, structured output refers to the practice of having language models return responses in a well-defined data format (for example, JSON), rather than free-form text. This makes the model output easier to parse and work with programmatically.

```text
[Prompt] - Can you create a one-day travel itinerary for Paris?

[Text (LLMs Unstructured Response)] 
Here's a suggestion itinerary: Morning: Visit the Eiffel Tower.
Afternoon: Walk through the Louvre Museum.
Evening: Enjoy dinner at a Seine riverside cafe.

[JSON enforced output (LLMs Structured Response)]
[
    {"time": "Morning", "activity": "Visit the Eiffel Tower"},
    {"time": "Afternoon", "activity": "Walk through the Louvre Museum."},
    {"time": "Evening", "activity": "Enjoy dinner at a Seine riverside cafe."}
]
```
Why do we need `structured output` ?
- Data Extraction
- API Building
- Agents

Ways to get structured output: There are 2 types of LLMs in this context one is the LLM which can generate structured output (ChatGPT, Claude) and one is which can't generate structured output by default.
Langchain provides 2 methods for these for who can generate structured output `with_structured_output` and for who can't generate structured output `Output Parser`

#### with_structured_output ---> data_format
Multiple ways of validation: Typed Dict, Pydantic, Json_schema

`TypedDict` is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.

Why use TypeDict ?
- It tells Python what keys are required and what types of values they should have.
- It does not validate data at runtime (it just helps with type hints for better coding.)

Why use Annotated ?
- It provided context with type checking, it take first input as datatype 

Why use Optional ?
- In case the provided context is optional or you can say the output is not decided it can be or not

Why use Literal ?
- In this we can give options 

`Pydantic` is a data validation and data parsing library for python. It ensures that the data you work with correct, structured, and type-safe.

`JSON Schema` validation is a way to define the structure and rules for JSON data. It allows you to specify required fields, data types, formats, and constraints to ensure that the input data is valid and consistent. By using a schema, systems can automatically validate incoming data, catch errors early, and enforce standards across applications.
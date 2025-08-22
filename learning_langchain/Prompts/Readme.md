# Prompts

Prompts are the input instructions or queries given to a model to guide its output.  
Well-crafted prompts directly influence the **quality, style, and structure** of the model’s response.

---

#### Types of Prompts
- **Text-based**
- **Multimodal** (image / sound / video)
   > Example: Providing an image and asking the model to describe it.
---

#### Static vs Dynamic Prompts
- **Static Prompts** – Fixed text that never changes.
- **Dynamic Prompts** – Generated or modified at runtime, often using variables or data from user input.
  > Example: "Summarize the article titled `{article_title}`."

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
1. **Default validation** – Ensures required variables are provided. Unlike f-strings, missing variables will raise an error early.
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

This diagram shows how LangChain handles both single prompts and multi-turn conversations.

___

#### Messages

* **System Message** – Message for priming AI behavior. Usually passed as the first of a sequence of input messages.
  > Example: “You are a helpful assistant.”
* **Human Message** – Message from a human. Passed from the user to the model.
  > Example: “Explain quantum physics in simple terms.”
* **AI Message** – Message from an AI. Returned from a chat model as a response to a prompt.
  This message contains:

  * The raw output from the model.
  * Standardized fields (e.g., tool calls, usage metadata) added by LangChain.

---

#### Message Placeholder

A **Message Placeholder** in LangChain is a special placeholder used inside a `ChatPromptTemplate` to dynamically insert chat history or a list of messages at runtime. This helps maintain context in conversations without manually concatenating messages.


## Structure Output
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
- Data Extraction : Cleanly extract key information.
- API Building : Models can serve as backends for apps.
- Agents : Agents rely on structured outputs for decision-making.

### Ways to get structured output
There are 2 types of LLMs in this context one is the LLM which can generate structured output (ChatGPT, Claude) and one is which can't generate structured output by default.

LangChain provides 2 methods:
- with_structured_output – For models that natively support structured responses.
- Output Parser – For models that don’t guarantee structure.

### with_structured_output
Multiple ways of validation: Typed Dict, Pydantic, Json_schema

`TypedDict` is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.

Why use TypeDict ?
- It tells Python what keys are required and what types of values they should have.
- It does not validate data at runtime (it just helps with type hints for better coding.)

Why use Annotated ?
- It provided context with type checking, it takes first input as datatype  or you can say adds context with type checking.

Why use Optional ?
- In case the provided context is optional, or you can say the output is not decided it can be or not. Basically marks fields as not strictly required. 

Why use Literal ?
- In this we can give options or you can say restricts values to specific options. 

___

`Pydantic` is a data validation and data parsing library for python. It ensures that the data you work with correct, structured, and type-safe.

___

`JSON Schema` validation is a way to define the structure and rules for JSON data. It allows you to specify required fields, data types, formats, and constraints to ensure that the input data is valid and consistent. By using a schema, systems can automatically validate incoming data, catch errors early, and enforce standards across applications.

#### When to use what?

Use **TypedDict** if:
- You only need type hints (basic structure enforcement)
- You don't need validation (e.g., checking numbers are positive)
- You trust the LLM to return correct data

Use **Pydantic** if:
- You need data validation (e.g., sentiment must be "positive" or "negative")
- You need default values if the LLM misses fields
- You want automatic type conversion (e.g., "100" → 100)

Use **JSON Schema** if:
- You don't want to import extra Python libraries (like Pydantic)
- You need validation but don't need Python objects
- You want to define structure in a standard JSON format

| Feature                | TypedDict | Pydantic | JSON Schema |
|------------------------|-----------|----------|--------------|
| Data Validation        | false     | true     | true         |
| Default Values         | false     | true     | false        |
| Automatic Conversion   | false     | true     | false        |
| Cross-language Support | false     | false    | true         |

---

`methods` with_structured_output support two types of methods one is json_schema this will give output in json_schema and one is function calling use function calling when your output calling a function. Some models give json structured output while some doesn't give and some models are not even give structured output. 


### Output Parser

Output Parser in Langchain help convert raw LLM responses into structured formats like JSON, CSV, Pydantic models and more. They ensure consistency, validation and ease of use in application.

Types of Output Parser
- `StringOutputParser`
  The StrOutputParser is the simplest output parser in Langchain. It is used to parse the output of a LLM and return it as plain string.

- `JSONOutputParser`
  It is used to parse the output of a LLM and return it as a json. One of the drawbacks of JSONOutputParser is that it doesn't enforce a schema it means we can't decide what will be the exact format of json it's on LLM.

- `StructuredOutputParser`
  It is an output parser in Langchain that helps extract structured JSON data from LLM response based on predefined fields schema.
  It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured output.
  Disadvantage of this parser is that there is no way of data validation.

- `PydanticOutputParser`
  It is a structured output parser in Langchain that uses Pydantic models to enforce schema validation when processing LLM response.

  - **Strict Schema Enforcement** : Ensures that LLM response follow a well-defined structure.
  
  - **Type Safety** : Automatically converts LLM outputs into Python objects.
  
  - **Easy Validation** : Uses Pydantic's built-in validation to catch incorrect or missing data.
  
  - **Seamless Integration** : Works well with other Langchain components.


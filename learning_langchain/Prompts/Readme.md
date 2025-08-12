# Prompts

Prompts are the input instructions or queries given to a model to guide its output.

### Types of Prompts
- **Text-based**
- **Multimodal** (image / sound / video)

### Static vs Dynamic Prompts
- **Static Prompts** – Fixed text that never changes.
- **Dynamic Prompts** – Generated or modified at runtime, often using variables or data from user input.

---

### Prompt Template

A **PromptTemplate** in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template.  
Instead of hardcoding prompts, `PromptTemplate` allows you to define **placeholders** that can be filled at runtime with different values.

This makes it:
- **Reusable**
- **Flexible**
- **Easy to manage**, especially when working with dynamic user inputs or automated workflows.

---

#### Why use `PromptTemplate` over f-strings?
1. **Default validation** – Ensures required variables are provided.(PromptTemplate(
    template="""<prompt>""", input_variables=<input-variable>, validate_template=True)
2. **Reusability** – Easily reuse prompt structures in different contexts.
3. **LangChain ecosystem compatibility** – Integrates smoothly with LangChain tools and chains.

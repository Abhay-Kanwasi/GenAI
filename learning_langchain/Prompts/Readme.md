# Prompts are the input instructions or queries given to a model to guide it's output

- Text based 
- Multimodal (image / sound / video)

static vs dynamic prompts

### Prompt Template
A PromptTemplate in Langchain is a structured way to create prompts dynamically by inserting variables into predefined template. Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different paths.

This make it reusable, flexible, and easy to manage, especially when working with dynamic user inputs or automated workflows.

Why use PromptTemplate over f string >
1. Default validation
2. Reusable
3. LangChain Ecosystem
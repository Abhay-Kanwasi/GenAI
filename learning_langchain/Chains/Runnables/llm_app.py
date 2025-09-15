from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the LLM
llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0.7)

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

topic = input('Enter a topic: ')

# Format the prompt manually using PromptTemplate
formatted_input = prompt.format(topic=topic)

blog_title = llm.predict(formatted_input)

print("Generated Blog Title:", blog_title)


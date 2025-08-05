from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

user_input = "What is model in context of langchain?"

user_output = llm.invoke(user_input)
print(user_output)
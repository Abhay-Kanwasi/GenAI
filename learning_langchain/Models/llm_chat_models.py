from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() # It will only locate key if .env contains OPENAI_API_KEY variable.

model = ChatOpenAI(model='gpt-4', temperature=0.8)

user_input = "What is model in context of langchain?"

user_output = model.invoke(user_input)
print(user_output.content)
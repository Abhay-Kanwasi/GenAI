from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')

user_input = "What is model in context of langchain?"

user_output = model.invoke(user_input)
print(user_output.content)
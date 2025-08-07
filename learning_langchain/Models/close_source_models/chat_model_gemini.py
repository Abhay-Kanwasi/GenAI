from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()  # GOOGLE_API_KEY

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

user_input = "What are indexes in context of LLM"

user_output = model.invoke(user_input)

print(user_output)

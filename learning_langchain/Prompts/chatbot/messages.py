from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are helpful assistant.'),
    HumanMessage(content='Tell me about Langchain')
]

results = model.invoke(messages)
messages.append(AIMessage(content=results.content))
print(messages)

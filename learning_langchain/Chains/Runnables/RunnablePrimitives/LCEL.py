# LCEL : LangChain Expression Language : It is mainly a new way of creating RunnableSequence instead or RunnableSequence(r1, r2, r3..) we will be creating sequence like this.. r1 | r2 | r3

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

# 1. Define the Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "Tell me a fun fact about {topic}."),
])

# 2. Define the Language Model
# Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
llm = ChatOpenAI(openai_api_key="YOUR_OPENAI_API_KEY", temperature=0.7)

# 3. Define the Output Parser
output_parser = StrOutputParser()

# 4. Construct the LCEL Chain
# The pipe operator (|) chains the components together
chain = prompt | llm | output_parser

# 5. Invoke the Chain
response = chain.invoke({"topic": "cats"})

# 6. Print the result
print(response)
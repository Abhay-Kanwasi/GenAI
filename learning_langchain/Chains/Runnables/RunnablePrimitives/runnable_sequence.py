from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables=['topic'],
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)
topic = 'ai'
response = chain.invoke({'topic': topic})
print(f'Joke is about {topic}.\n: Joke is :{response}')

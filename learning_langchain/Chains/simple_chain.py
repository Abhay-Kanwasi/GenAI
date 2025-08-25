from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

results = chain.invoke({'topic' : 'Cricket'})

print(f'Result after parsing: {results}\n')

print("\nVisualizing the chain\n")
print(chain.get_graph().print_ascii())
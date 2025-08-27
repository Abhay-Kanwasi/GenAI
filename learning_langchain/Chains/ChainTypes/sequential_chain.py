# This is as simple chain but instead of one we use 2 LLMs

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


load_dotenv()

report_prompt = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic'],
)

summary_prompt = PromptTemplate(
    template='Generate a 5 point summary report from the following text \n {topic}',
    input_variables=['text'],
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = report_prompt | model | parser | summary_prompt | model | parser

results = chain.invoke({'topic': "Future of AI"})
print(f'Results: {results}')

print("\nVisualizing the chain\n")
chain.get_graph().print_ascii()
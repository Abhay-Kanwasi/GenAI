from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

# Prompt to detailed report
report_template = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

# Prompt to summary
summary_template = PromptTemplate(
    template="Write 5 line summary on the following text.\n {text}",
    input_variables=['text']
)

report_prompt = report_template.invoke({'topic' : 'black hole'})

report = model.invoke(report_prompt)
print(f'Report: {report.content}')

summary_prompt = summary_template.invoke({'text' : report.content})

summary = model.invoke(summary_prompt)

# print(f'\n\nOverall Summary {summary.content}')

# Do the above thing using chain and string output parser
parser = StrOutputParser()

chain = report_template | model | parser | summary_template | model | parser

parsed_summary = chain.invoke({'topic': 'black hole'})

print(f'Parsed summary {parsed_summary}')
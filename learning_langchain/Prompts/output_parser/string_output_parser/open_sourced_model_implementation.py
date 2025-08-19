from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
)

model = ChatHuggingFace(llm=llm)

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

summary_prompt = summary_template.invoke({'text' : report.content})

summary = model.invoke(summary_prompt)

print(summary.content)
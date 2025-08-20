from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
json_parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': json_parser.get_format_instructions()},
)

prompt = template.format()

print(f"Prompt: {prompt}")

before_parsing_result = model.invoke(prompt)

print(f"Result before parsing : {before_parsing_result}")

after_parsing_results = json_parser.parse(before_parsing_result.content)
print(f"Result after parsing : {after_parsing_results}")

# Or we can do this using chain
chain = template | model | json_parser

results_using_chian = chain.invoke({}) # Even you don't have any input values you have to pass an empty dictionary
print(f"Result using Chian : {results_using_chian}")
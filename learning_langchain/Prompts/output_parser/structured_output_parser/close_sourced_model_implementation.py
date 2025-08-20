from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name="Fact 1", description="Fact 1 about the topic"),
    ResponseSchema(name="Fact 2", description="Fact 2 about the topic"),
    ResponseSchema(name="Fact 3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about the {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

prompt = template.invoke({'topic' : 'Black Hole'})
print(f"Prompt: {prompt}\n")

before_parsing_result = model.invoke(prompt)
print(f"Result before parsing : {before_parsing_result}\n")

after_parsing_result = parser.parse(before_parsing_result.content)
print(f"Result after parsing : {after_parsing_result}\n")

# Doing it with chain
chain = template | model | parser
results_from_chain = chain.invoke({"topic" : "Black Hole"})
print(f"Result from chain: {results_from_chain}\n")
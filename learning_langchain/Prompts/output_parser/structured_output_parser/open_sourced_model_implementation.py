import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
hf_token = os.getenv("HF_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    huggingfacehub_api_token=hf_token,
)

model = ChatHuggingFace(llm=llm)

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
print(f"Prompt: {prompt}")

before_parsing_result = model.invoke(prompt)
print(f"Result before parsing : {before_parsing_result}")

after_parsing_result = parser.parse(before_parsing_result.content)
print(f"Result after parsing : {after_parsing_result}")

# Doing it with chain
chain = template | model | parser
results_from_chain = chain.invoke({"topic" : "Black Hole"})
print(f"Result from chain: {results_from_chain}")
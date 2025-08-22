import os
from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field


from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="Person's name")
    age: int = Field(gt=18, description="Person's age")
    city: str = Field(description="Person's city")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {origin} person\n {format_instructions}",
    input_variables=['origin'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

prompt = template.invoke({'origin': 'india'})
print(f'Prompt: {prompt}\n')

result_before_parsing = model.invoke(prompt)
print(f'Result before parsing: {result_before_parsing}\n')

result_after_parsing = parser.parse(result_before_parsing.content)
print(f'Result after parsing: {result_after_parsing}\n')

# Do this wih chain
chain = template | model | parser
result_from_chain = chain.invoke({'origin': 'japanese'})
print(f'Result from chain: {result_from_chain}\n')
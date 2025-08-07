from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()   # HUGGINGFACEHUB_ACCESS_TOKEN

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

user_input = "Generate a blog about Python"

llm_output = model.invoke(user_input)

print(llm_output)

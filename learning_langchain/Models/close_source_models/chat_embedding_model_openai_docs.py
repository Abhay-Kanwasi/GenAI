from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)  # dimensions decide the vector size (
# context)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

llm_output = embedding.embed_documents(documents)

print(str(llm_output))  # It's a vector output

# Note: By default embedding vector will be small 1536 large 3072

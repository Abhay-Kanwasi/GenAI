from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)  # dimensions decide the vector size (
# context)

user_query = "Delhi is the capital of India"

llm_output = embedding.embed_query(user_query)

print(str(llm_output))  # It's a vector output

# Note: By default embedding vector will be small 1536 large 3072

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "This is getting the input for local embedding model"

documents = [
    "First line of the document",
    "Second line of the document",
    "Third line of the document",
]

query_vector = embedding.embed_query(text)
print(str(query_vector))

document_vector = embedding.embed_documents(documents)
print(str(document_vector))
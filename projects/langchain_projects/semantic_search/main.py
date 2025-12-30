# Build a semantic search engine with LangChain

import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.runnables import chain
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore

# Load documents
file_path = "nke-10k-2023.pdf"  
print(f'file path exists {os.path.exists(file_path)}')

loader = PyPDFLoader(file_path)
docs = loader.load()

# Splitting
"""
For both information retrieval and downstream question-answering purposes, a page may be too coarse a representation. Our goal in the end will be to retrieve Document objects that answer an input query, and further splitting our PDF will help ensure that the meanings of relevant portions of the document are not “washed out” by surrounding text.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

print(f'number of splits {len(all_splits)}')

# Embedding
"""
Vector search is a common way to store and search over unstructured data (such as unstructured text). The idea is to store numeric vectors that are associated with the text. Given a query, we can embed it as a vector of the same dimension and use vector similarity metrics (such as cosine similarity) to identify related text.
"""

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_1 = embeddings.embed_query(all_splits[0].page_content)
vector_2 = embeddings.embed_query(all_splits[1].page_content)

assert len(vector_1) == len(vector_2)
print(f"fenerated vectors of length {len(vector_1)}\n")

# Vector stores
"""
LangChain VectorStore objects contain methods for adding text and Document objects to the store, and querying them using various similarity metrics. They are often initialized with embedding models, which determine how text data is translated to numeric vectors.
"""

vector_store = InMemoryVectorStore(embeddings)

# Having instantiated our vector store, we can now index the documents.
ids = vector_store.add_documents(documents=all_splits)

# Retrievers
"""
LangChain VectorStore objects do not subclass Runnable. LangChain Retrievers are Runnables, so they implement a standard set of methods (e.g., synchronous and asynchronous invoke and batch operations). Although we can construct retrievers from vector stores, retrievers can interface with non-vector store sources of data, as well (such as external APIs).
"""
@chain
def retriever(query: str) -> List[Document]:
    return vector_store.similarity_search(query, k=1)

question = input("Question : ")
answer = retriever.batch(
    [
        question
    ],
)

doc = answer[0][0]
print(doc.page_content)
text = doc.page_content
for line in text.split("."):
    if "incorporated" in line.lower():
        print(line.strip() + ".")

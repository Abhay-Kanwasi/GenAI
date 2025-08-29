from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

loader = TextLoader("docs.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50) # in parts
docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings()) # generate embeddings

retriever = vectorstore.as_retriever()

query = "What are the key takeaways from the document?"
retrieved_documents = retriever.get_relevant_documents(query)
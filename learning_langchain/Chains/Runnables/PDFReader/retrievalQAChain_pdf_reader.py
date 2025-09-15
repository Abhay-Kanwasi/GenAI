from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

loader = TextLoader("docs.txt")
documents = loader.load()

# Split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50) # in parts
docs = text_splitter.split_documents(documents)

# Convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings()) # generate embeddings

# Create a retriever (fetches relevant documents)
retriever = vectorstore.as_retriever()

# Initialize LLM
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Create RetrievalQAChain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "What is the whole summary of the document ?"
answer = qa_chain.run(query)
print(f"Answer: {answer}")
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

# Manually retrieve relevant documents
query = "What are the key takeaways from the document?"
retrieved_documents = retriever.get_relevant_documents(query)

# Combine retrieved text into single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_documents])

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Manually pass retrieved text to LLM
prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)

# Print the answer
print(f"Answer: {answer}")
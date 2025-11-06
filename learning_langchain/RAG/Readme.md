# RAG 

RAG is a technique that combines information retrival with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded response.

Benefits of using RAG

1. Use of up-to-date information
2. Better Privacy
3. No limit of document size

## Components of RAG

### Document Loader
Document loaders are components in LangChain used to load data (there are multiple data sources) from various sources into a standardized format (usually as Document objects), which can then be used for chunking, embedding, retrieval and generation. Most document loader give output as list.

Example: Document(page_content="This is a page content", metadata={"source":"filename.pdf", ...})

#### Types of Document Loader
1. `Text Loader` is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects. 

- Use Case
  - Ideal for loading chat logs, scraped text, transcript, code snippets or any plain text data into a LangChain pipeline.
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

- Limitation
  - Works only with .txt files

2. `PyPDFLoader` is a document loader in LangcChain used to load content from PDF files and convert each page into Document object

```text
[
  Document(page_content="Page 1 content", metadata={"page":0, "source":"file.pdf"}),
  Document(page_content="Page 2 content", metadata={"page":1, "source":"file.pdf"}),
]
```

- Limitations:
  - It uses the PyPDF library under the hood - not great with Scanned PDF or complex layouts.

||      Use Case                  || Recommended Loader                               ||
|| Simple, clean PDFs             || PyPDFLoader                                      ||
|| PDFs with tables/columns       || PDFPlumberLoader                                 ||
|| Scanned/image PDFs             || UnstructuredPDFLoader or AmazonTextractPDFLoader ||
|| Need layout and image data     || PyMuPDFLoader                                    ||
|| Want best structure extraction || UnstructuredPDFLoader                            ||

3. `DirectoryLoader` is document loader that lets you load multiple documents from a directory (folder) of files.

Glob Pattern || What it loads 
""**/*.txt"" || All .txt files in all subfolders 
"*.pdf"      || All .pdf files in the root folder
"data/*.csv" || All .csv files in the data/ folder
"**/*"       || All files (any type, all folders)
**           || Recursive search through subfolders 

<h3>Load vs Lazy Load</h3>

load()                                         || lazy_load()

Eager loading (load everything at once)        || Lazy loading (loads on demand).
Returns: A list of Document objects            || Returns: A generator of Document objects
Loads all documents immediately into memory.
Best when: 
  - The number of documents is small.
  - You want everything loaded upfront.

### Text Splitter

Text splitting is the process of breaking large chunks of text(like articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.

- Overcoming model limitations: Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.
- Downstream tasks: Text Splitting improves nearly every LLM powered task

Task                | Why Splitting helps
Embedding           | Short chunks yield more accurate vectors       
Semantic Search     | Search results point to focused info, not noise
Summarization       | Prevents hallucination and topic drift

- Optimizing computational resources: Working with smaller chunks of text can be more memory-efficient and allow better parallelization of processing tasks.

1. Length based text splitting
2. Text structured based 

### Document Structured Based
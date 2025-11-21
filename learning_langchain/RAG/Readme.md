# RAG

RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.

---

## Benefits of Using RAG

1. Use of up-to-date information
2. Better privacy
3. No limit on document size

---

## Components of RAG

### Document Loader

Document loaders are components in LangChain used to load data from various sources into a standardized format (usually as `Document` objects), which can then be used for chunking, embedding, retrieval, and generation. Most document loaders output a list.

**Example:**

```python
Document(page_content="This is a page content", metadata={"source": "filename.pdf", ...})
```

#### Types of Document Loader

**1. Text Loader**

A simple and commonly used document loader in LangChain that reads plain text (`.txt`) files and converts them into `Document` objects.

* **Use Case:**
  Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.

* **Limitation:**
  Works only with `.txt` files.

---

**2. PyPDFLoader**

A document loader in LangChain used to load content from PDF files and convert each page into a `Document` object.

```python
[
  Document(page_content="Page 1 content", metadata={"page": 0, "source": "file.pdf"}),
  Document(page_content="Page 2 content", metadata={"page": 1, "source": "file.pdf"}),
]
```

* **Limitations:**
  Uses the PyPDF library under the hood — not ideal for scanned PDFs or complex layouts.

<br />

| Use Case                   | Recommended Loader                               |
| -------------------------- | ------------------------------------------------ |
| Simple, clean PDFs         | PyPDFLoader                                      |
| PDFs with tables/columns   | PDFPlumberLoader                                 |
| Scanned/image PDFs         | UnstructuredPDFLoader or AmazonTextractPDFLoader |
| Need layout and image data | PyMuPDFLoader                                    |
| Best structure extraction  | UnstructuredPDFLoader                            |

---

**3. DirectoryLoader**

A document loader that lets you load multiple documents from a directory (folder) of files.

| Glob Pattern | What It Loads                          |
| ------------ | -------------------------------------- |
| `**/*.txt`   | All `.txt` files in all subfolders     |
| `*.pdf`      | All `.pdf` files in the root folder    |
| `data/*.csv` | All `.csv` files in the `data/` folder |
| `**/*`       | All files (any type, all folders)      |
| `**`         | Recursive search through subfolders    |

---

### Load vs Lazy Load

| Method        | Description                                                                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `load()`      | Eager loading (loads everything at once). Returns a list of `Document` objects. Best when the number of documents is small or you want everything loaded upfront. |
| `lazy_load()` | Lazy loading (loads on demand). Returns a generator of `Document` objects. Useful for large datasets.                                                             |
Best when: - The number of documents is small. - You want everything loaded upfront.
---

### Text Splitter

Text splitting is the process of breaking large chunks of text (like articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.

**Why It’s Important:**

* **Overcoming model limitations:** Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.
* **Downstream tasks:** Text splitting improves nearly every LLM-powered task.

| Task            | Why Splitting Helps                             |
| --------------- | ----------------------------------------------- |
| Embedding       | Short chunks yield more accurate vectors        |
| Semantic Search | Search results point to focused info, not noise |
| Summarization   | Prevents hallucination and topic drift          |

* **Optimizing computational resources:** Working with smaller chunks of text can be more memory-efficient and allow better parallelization of processing tasks.

**Types of Text Splitting:**

1. Length-based text splitting
2. Text structure-based (Split text based on text structural hierarchy)
3. Document structure-based (Used for different type of text formats like markdown, programming languages)
4. Semantic meaning-based (Used when text contain completely different topics)

---

### Vector Store

A vector store is a system designed to store and retrieve data represented as numerical vectors.

**Key Features**

1. **Storage** – Ensures that vectors and their associated metadata are retained, whether in-memory for quick lookups or on-disk for durability and large-scale use.
2. **Similarity Search** – Retrieves vectors most similar to a query vector.
3. **Indexing** – Provides structures or methods enabling fast similarity searches (e.g., approximate nearest neighbor lookups).
4. **CRUD Operations** – Manage the lifecycle of data: adding, reading, updating, and removing vectors.

**Use Cases**

1. Semantic Search
2. RAG
3. Recommender Systems
4. Image/Multimedia Search

---

### Vector Store vs Vector Database

A **Vector Store** provides in-memory or file-based storage and retrieval, while a **Vector Database** adds advanced features like scalability, persistence, clustering, and hybrid search capabilities.

#### Vector Store
- Typically refers to a lightweight library or service that focuses on storing vectors (embedding) and performing similarity search.
- May not include many traditional database features like transactions, rich query languages or role-based access control.
- Ideal for prototyping, smaller-scale applications.
- Examples: FAISS where you store vectors and can query them by similarity, but you handle persistance and scalling seperately.

#### Vector Database
- A full-fledged database system designed to store and query vectors.
- Offers additional "database-like" features:
  - Distributed architecture for horizontal scaling
  - Durability and persistence (replication, backup/restore)
  - Metadata handling (schemas, filters)
  - Potential for ACID or near-ACID guarantees
  - Authentication/authorization and more advanced security

- Geared for production environments with significant scaling, large datasets
- Examples: Milvus, Qdrant, Weaviate

A vector database is effectively a vector store with extra database features (e.g.,
clustering, scaling, security, metadata filtering, and durability)

---

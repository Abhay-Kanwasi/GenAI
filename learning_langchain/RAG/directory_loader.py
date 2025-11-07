from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# This code does three things:
# 1. Goes to the 'adhar_card' folder
# 2. Finds all PDF files
# 3. Reads each PDF page by page

loader = DirectoryLoader(
    path='adhar_card',        # The folder to look in
    glob='*.pdf',        # Only files ending with .pdf
    loader_cls=PyPDFLoader  # How to read PDF files
)

# lazy_load() is memory-friendly - loads one document at a time
documents = loader.lazy_load()

print("Reading PDF files from 'adhar_card' folder...")
print("Here's the information about each page:\n")

# Go through each PDF page one by one
counter = 1
for doc in documents:
    print(f"Page {counter}:")
    print(f"  File: {doc.metadata.get('source', 'Unknown')}")
    print(f"  Page number: {doc.metadata.get('page', 'Unknown')}")
    print(f"  Content preview: {doc.page_content[:100]}...")  # First 100 chars
    print("-" * 60)
    counter += 1
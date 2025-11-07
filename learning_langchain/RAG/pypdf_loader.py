from langchain_community.document_loaders import PyPDFLoader

# This code loads a PDF file and shows basic information about it

print("Starting PDF loading process...")

# Create a PDF loader for our file
loader = PyPDFLoader('your-pdf-file-name.pdf')

# Load all pages from the PDF
documents = loader.load()

# Show how many pages we have
print(f"\nThe PDF has {len(documents)} pages")

# Show the content of the first page
print("\n" + "=" * 50)
print("CONTENT OF PAGE 1:")
print("=" * 50)
print(documents[0].page_content)

# Show the metadata of the second page
print("\n" + "=" * 50)
print("METADATA OF PAGE 2:")
print("=" * 50)

if len(documents) > 1:
    print(f"Source: {documents[1].metadata.get('source', 'Unknown')}")
    print(f"Page number: {documents[1].metadata.get('page', 'Unknown')}")
else:
    print("Document has only one page")

# Quick overview of all pages
print("\n" + "=" * 50)
print("QUICK OVERVIEW:")
print("=" * 50)
for i, doc in enumerate(documents):
    words = len(doc.page_content.split())
    print(f"Page {i+1}: {words} words, {len(doc.page_content)} characters")
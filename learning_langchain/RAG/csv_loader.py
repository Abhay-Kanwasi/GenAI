from langchain_community.document_loaders import CSVLoader

# Think of this like opening a CSV file in Excel
# But instead of seeing a spreadsheet, we get "documents" - one for each row
loader = CSVLoader(file_path='Social_Network_Ads.csv')

# Convert the spreadsheet into a list of documents
# Each row becomes one document that AI can understand
documents = loader.load()

# Check how many rows we have
print(f"We loaded {len(documents)} rows from the CSV file")

# Look at what the second row contains
print("\nHere's what the second row looks like as a document:")
print("Content:", documents[1].page_content)
print("Metadata:", documents[1].metadata)
# Import necessary libraries
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

# Load environment variables (for OpenAI API key)
load_dotenv()

print("Initializing AI components...")

# Initialize the AI model
model = ChatOpenAI(model="gpt-3.5-turbo")  # You can specify the model

# Create a prompt template that tells the AI how to format its response
prompt = PromptTemplate(
    template="""
    Based on the following text content, please answer the question clearly and concisely.
    
    TEXT CONTENT:
    {text}
    
    QUESTION: {question}
    
    ANSWER:
    """,
    input_variables=['question', 'text']
)

# Initialize output parser to get clean string responses
parser = StrOutputParser()

print("AI components initialized successfully!\n")

# Using a Wikipedia article about Artificial Intelligence (more content-rich)
url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'

print(f"Loading content from: {url}")
loader = WebBaseLoader(url)

# Load the web page content
docs = loader.load()
print(f"Successfully loaded web content!")
print(f"Content length: {len(docs[0].page_content)} characters\n")

# Create the processing chain: Prompt -> Model -> Parser
chain = prompt | model | parser

print("Asking questions about the content...\n")

# Ask specific questions about the loaded content
questions = [
    "What is the main topic of this article?",
    "What are some key applications mentioned?",
    "What is the historical background provided?"
]

for question in questions:
    print(f"Q: {question}")
    
    # Invoke the chain with the question and web content
    answer = chain.invoke({
        'question': question, 
        'text': docs[0].page_content[:4000]  # Using first 4000 chars to avoid token limits
    })
    
    print(f"A: {answer}")
    print("-" * 80 + "\n")
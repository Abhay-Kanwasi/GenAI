from dotenv import load_dotenv
from typing import Literal
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda

# Load environment variables
load_dotenv()

# Initialize model & parsers
model = ChatOpenAI()
string_output_parser = StrOutputParser()

# Define Feedback schema (for classification)
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback: positive or negative"
    )

pydantic_output_parser = PydanticOutputParser(pydantic_object=Feedback)

# Prompt to classify sentiment
classify_prompt = PromptTemplate(
    template=(
        "Classify the sentiment of the following text into positive or negative.\n"
        "Text: {feedback}\n"
        "{format_instruction}"
    ),
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": pydantic_output_parser.get_format_instructions()
    },
)

# Classifier chain: feedback → sentiment (Pydantic object)
classifier_chain = classify_prompt | model | pydantic_output_parser

# Example check (uncomment to debug classification result)
# user_sentiment = classifier_chain.invoke({'feedback': 'This is the terrible smart phone.'})
# print(f'User Sentiment: {user_sentiment}')
# → Feedback(sentiment="negative")

# Prompts for generating responses
positive_prompt = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}\n",
    input_variables=["feedback"],
)

negative_prompt = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}\n",
    input_variables=["feedback"],
)

# Branch logic
# RunnableBranch takes classifier output (Feedback object) and decides path
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_prompt | model | string_output_parser),
    (lambda x: x.sentiment == "negative", negative_prompt | model | string_output_parser),
    RunnableLambda(lambda x: "Could not find sentiment"),
)

# Final chain = classification → branch
final_chain = classifier_chain | branch_chain

# Run example
user_feedback = "This is the wonderful smart phone."
print("\nUser feedback:", user_feedback)
print("\nAI Response:", final_chain.invoke({"feedback": user_feedback}))

# Visualize chain graph
print("\nVisualizing the chain\n")
final_chain.get_graph().print_ascii()

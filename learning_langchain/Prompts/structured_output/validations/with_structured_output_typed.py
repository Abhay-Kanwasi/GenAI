from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

product_review = """
    The design and build are excellent, but the software is cluttered. Too many unwanted apps come pre-installed and can’t be removed. The interface also feels dated. A software update could fix this.
    
    Performance is great, but the system feels overloaded. There are several preloaded apps that I’ll never use and can’t uninstall. The UI looks behind the times. Hoping for improvements in future updates.
    
    The device runs smoothly, but the software feels unnecessarily heavy. Too many built-in apps are locked in place, 
    and the visuals look old. A cleaner, more modern update is much needed.
    
    Love the hardware, but the software is messy. It’s full of pre-installed apps I can’t delete, and the user interface 
    feels stuck in the past. Waiting for a major software refresh.
    
    The build quality is top-notch, but the software leaves much to be desired. Too many non-removable apps and an 
    outdated design spoil the experience. A timely update could change that.
"""


# Schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive and neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)  # When we use with_structured_output method it generates
# prompt behind the scene and give summary and sentiment, so it can give a structured output
results = structured_model.invoke(product_review)

print(results['summary'])
print(results['sentiment'])

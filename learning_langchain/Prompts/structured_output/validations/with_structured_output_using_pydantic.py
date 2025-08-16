from typing import Optional, Literal
from pydantic import BaseModel, Field

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):
    key_themes: list[str] = Field(description = "Write down all the key themes discussed in the review in a list")
    summary: str = Field(description = "A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description = "Return sentiment of the review either negative, positive and neutral")
    pros: Optional[list[str]] = Field(description = "Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(description = "Write down all the cons inside a list")
    name: Optional[str] = Field(description = "Write the name of the reviewer")

product_review = """
    The design and build are excellent, but the software is cluttered. Too many unwanted apps come pre-installed and can’t be removed. The interface also feels dated. A software update could fix this.

    Performance is great, but the system feels overloaded. There are several preloaded apps that I’ll never use and can’t uninstall. The UI looks behind the times. Hoping for improvements in future updates.

    The device runs smoothly, but the software feels unnecessarily heavy. Too many built-in apps are locked in place, 
    and the visuals look old. A cleaner, more modern update is much needed.

    Love the hardware, but the software is messy. It’s full of pre-installed apps I can’t delete, and the user interface 
    feels stuck in the past. Waiting for a major software refresh.

    The build quality is top-notch, but the software leaves much to be desired. Too many non-removable apps and an 
    outdated design spoil the experience. A timely update could change that.
    
    By ChatGPT
"""

structured_model = model.with_structured_output(Review)  # When we use with_structured_output method it generates

# prompt behind the scene and give summary and sentiment, so it can give a structured output
results = structured_model.invoke(product_review)

print(results.name) # It will print ChatGPT
print(dict(results))
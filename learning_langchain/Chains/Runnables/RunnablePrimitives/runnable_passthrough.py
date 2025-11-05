"""
    RunnablePassthrough is a simple runnable in LangChain that returns the input as output without any modifications. It is useful for testing and debugging purposes, or when you want to create a placeholder runnable in a chain or workflow.

    Suppose we want to create a joke explanation of any topic but in this scenario we will be getting only the joke explanation not the original joke.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# Example usage of RunnablePassthrough
passthrough_runnable = RunnablePassthrough()
print(passthrough_runnable.invoke(2))

# Creating a chain that generates a joke and then explains it using RunnablePassthrough
joke_prompt = PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables=['topic'],
)
explanation_prompt = PromptTemplate(
    template='Explain the following joke: {joke}',
    input_variables=['joke'],
)   

model = ChatOpenAI()

parser = StrOutputParser()

joke_generation_chain = RunnableSequence(joke_prompt, model, parser)

parllel_chain = RunnableSequence({
    'joke': joke_generation_chain,
    'explanation': RunnableSequence(
        explanation_prompt,
        model,
        parser
    )
})

final_chain = RunnableSequence(joke_generation_chain, parllel_chain)

print(final_chain.invoke({'topic': 'Apple'}))
"""
    RunnableParallel is a primitive in LangChain that allows you to run multiple runnables concurrently, enabling parallel processing of tasks. It is useful when you want to perform multiple operations simultaneously and aggregate their results. Each runnable receives the same input and process it independently, producing a directory of outputs.
    Suppose you have a topic AI you want one LLM to generate a tweet about it and another LLM to generate a linkedin post about the same topic.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

tweet_prompt = PromptTemplate(
    template='Generate a tweet about {topic}.',
    input_variables=['topic']
)

linkedin_prompt = PromptTemplate(
    template='Generate a linkedin post about {topic}.',
    input_variables=['topic']
)

model_for_tweet = ChatOpenAI()
model_for_linkedin = ChatOpenAI()

parser = StrOutputParser()

parllel_chain = RunnableParallel({
    'tweet': RunnableSequence(tweet_prompt, model_for_tweet, parser),
    'linkedin': RunnableSequence(linkedin_prompt, model_for_linkedin, parser), 
})

response = parllel_chain.invoke({'topic': 'AI'})
print(f"Tweet: {response['tweet']}\n")
print(f"Linkedin Post: {response['linkedin']}")
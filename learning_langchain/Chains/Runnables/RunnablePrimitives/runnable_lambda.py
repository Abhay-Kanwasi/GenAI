"""
    RunnableLambda is a runnable primitive that allows you to apply custom Python functions with an AI pipeline. It acts as a middleware between differnt AI components, enabling preprocessing, transformation, API calls, filtering and post-processing in a LangChain workflow.
    
    Suppose we want to create a joke about a specific topic. So user will be giving the topic and llm will generate a joke with character count in joke.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

from dotenv import load_dotenv

load_dotenv()

def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables=['topic'],
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parllel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
}) # or instead of using word counter we can use lambda function `lambda x: len(x.split())`

final_chain = RunnableSequence(joke_gen_chain, parllel_chain)
result = final_chain.invoke({'topic' : 'Agentic RAG'})
final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)
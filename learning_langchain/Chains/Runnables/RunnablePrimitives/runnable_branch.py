"""
    Runnable branch is a control flow component in Langchain that allows you to conditionally route input data to different chains or runnables based on custom logic.

    If funciton like an if/else/elif block for chains - where you define a set of condtion functions, each associated with a runnable (e.g. LLM call, prompt chain, or tool). The first matching condition matches, a default runnable is used (if provided).

    Suppose you have a topic and you want LLM to generate a report over it. If this report is greater than 500 words then we will tell LLM to summarize it and if less then 500 words then give as it is.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableBranch

from dotenv import load_dotenv

load_dotenv()

report_prompt = PromptTemplate(
        template='Write a detailed report on {topic}',
        input_variables=['topic']
    )

summary_prompt = PromptTemplate(
        template='Write a detailed report on {topic}',
        input_variables=['topic']
    )

model = ChatOpenAI()
parser = StrOutputParser()

report_gen_chain = RunnableSequence(report_prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(summary_prompt, model, parser)),
    default = RunnablePassthrough,
) 
# Syntax : RunnableBranch((tuple1), (tuple2), (tuple3)) and all the tuple will contain 2 things one is a condition and a runnable which # will execute if that condition is true. (condition, runnable) else a default runnable.
# e.g RunnableBranch(
    #    *branches: tuple[Callable, Runnable],
    #    
    # default: Runnable = None
#)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

final_chain.invoke({'topic' : 'India 2025 debt crisis'})
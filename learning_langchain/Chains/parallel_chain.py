from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

load_dotenv()

openai_model4 = ChatOpenAI()

openai_model3 = ChatOpenAI(model='gpt-3.5-turbo')

notes_generation_prompt = PromptTemplate(
    template='Generate and short and simple notes from the following text \n {text}',
    input_variables=['text']
)

short_question_and_answer_prompt = PromptTemplate(
    template="Generate 5 short questions answers from the following text \n {text}",
    input_variables=['text']
)

merge_both_prompt = PromptTemplate(
    template="Merged the provided notes and quiz into a single document \n {notes} and {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": notes_generation_prompt | openai_model4 | parser,
    "quiz": short_question_and_answer_prompt | openai_model3 | parser
})

final_chain = merge_both_prompt | openai_model4 | parser
full_chain = parallel_chain | final_chain

text = """
    LangChain is a software framework that helps facilitate the integration of large language models (LLMs) into applications. As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis.[2]

    History
    LangChain was launched in October 2022 as an open source project by Harrison Chase, while working at machine learning startup Robust Intelligence. The project quickly garnered popularity,[3] with improvements from hundreds of contributors on GitHub, trending discussions on Twitter, lively activity on the project's Discord server, many YouTube tutorials, and meetups in San Francisco and London. In April 2023, LangChain had incorporated and the new startup raised over $20 million in funding at a valuation of at least $200 million from venture firm Sequoia Capital, a week after announcing a $10 million seed investment from Benchmark.[4][5]

    In the third quarter of 2023, the LangChain Expression Language (LCEL) was introduced, which provides a declarative way to define chains of actions.[6][7]

    In October 2023 LangChain introduced LangServe, a deployment tool to host LCEL code as a production-ready API.[8]

    In February 2024 LangChain released LangSmith, a closed-source observability and evaluation platform for LLM applications, and announced a US $25 million Series A led by Sequoia Capital.[9] On 14 May 2025 the company launched LangGraph Platform into general availability, providing managed infrastructure for deploying long-running, stateful AI agents; the beta had already been used by nearly 400 companies.[10]

    Capabilities
    LangChain's developers highlight the framework's applicability to use-cases including chatbots,[11] retrieval-augmented generation,[12] document summarization,[13] and synthetic data generation.[14]

    As of March 2023, LangChain included integrations with systems including Amazon, Google, and Microsoft Azure cloud storage;[15] API wrappers for news, movie information, and weather; Bash for summarization, syntax and semantics checking, and execution of shell scripts; multiple web scraping subsystems and templates; few-shot learning prompt generation support; finding and summarizing "todo" tasks in code; Google Drive documents, spreadsheets, and presentations summarization, extraction, and creation; Google Search and Microsoft Bing web search;[16] OpenAI, Anthropic, and Hugging Face language models; iFixit repair guides and wikis search and summarization; MapReduce for question answering, combining documents, and question generation; N-gram overlap scoring; PyPDF, pdfminer, fitz, and pymupdf for PDF file text extraction and manipulation; Python and JavaScript code generation, analysis, and debugging; Milvus vector database[17] to store and retrieve vector embeddings; Weaviate vector database[18] to cache embedding and data objects; Redis cache database storage; Python RequestsWrapper and other methods for API requests; SQL and NoSQL databases including JSON support; Streamlit, including for logging; text mapping for k-nearest neighbors search; time zone conversion and calendar operations; tracing and recording stack symbols in threaded and asynchronous subprocess runs; and the Wolfram Alpha website and SDK.[19] As of April 2023, it can read from more than 50 document types and data sources.[20]
"""

result = full_chain.invoke({'text' : text})
print(f"Result: {result}")

print("\nVisualizing the chain\n")
full_chain.get_graph().print_ascii()


from langchain.llms import OpenAI
from langchain.chains import OpenAIChain
from langchain.prompts import PromptTemplate

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

chain = OpenAIChain(llm=llm, prompt=prompt)

topic = input("Enter a topic: ")
output = chain.run(topic)

print("Generated Blog Title:", output)
from langchain_core.prompts import ChatPromptTemplate

# This will create chat template but when you print if it's not taking argument values
# from langchain_core.messages import SystemMessage, HumanMessage
# chat_template = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple terms, what is {topic}')
# ])
"""Output: messages=[SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, 
response_metadata={}), HumanMessage(content='Explain in simple terms, what is {topic}', additional_kwargs={}, 
response_metadata={})]"""

# Use either ChatPromptTemplate(this is in latest version3) or ChatPromptTemplate.from_messages
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'wicket'})

print(prompt)

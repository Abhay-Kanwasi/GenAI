from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()  # ANTHROPIC_API_KEY

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

user_input = "What are chains in context of LLMs"

user_output = model.invoke(user_input)

print(user_output)

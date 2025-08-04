import asyncio

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient

from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math" : {
                "command" : "python",
                "args" : ["mathserver.py"], # Ensure absolute path
                "transport" : "stdio"
            },
            "weather" : {
                "url" : "http://localhost:8000/mcp", # Ensure the server is running
                "transport" : "streamable_http",

            }
        }
    )
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(
        model,
        tools
    )

    math_response = await agent.ainvoke(
        {"messages" : [{"role" : "user", "content" : "What is (3 + 5) x 12"}]}
    )

    weather_response = await agent.ainvoke(
        {"messages" : [{"role" : "user", "content" : "What is the weather in Dehradun(Uttarakhand, India)?"}]}
    )

    print(f"Math response: {math_response['messages'][-1].content}")
    print(f"Weather response : {weather_response['messages'][-1].content}")

asyncio.run(main())
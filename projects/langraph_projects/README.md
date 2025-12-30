# Agentic Langgraph

`Workflows` are systems where LLMs and tools are orchestrated through predefined code paths.

`Agents`, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

As agents gain more autonomy (less predefined control), their reliability may decrease, since decisions depend more on the LLM's reasoning rather than deterministic logic.

`Langgraph` is a framework that will help you to increase the reliability and build reliable agents. Provides a more expressive framework to build highly customizable, complex agents. Langgraph excels at graph based, stateful orchestration.  
e.g. multi-step, workflows with memory, streaming, human in the loop control.

> Langgraph vs Langchain

| Feature         | Langchain                                                 | Langgraph                                                              |
|-----------------|-----------------------------------------------------------|------------------------------------------------------------------------|
| Purpose         | Toolkit to build LLM apps (chains, tools, agents)         |                                                                        |
| Style           | Linear or reactive chains                                 | Graph-based, supports loops, retries, memory                           |
| Best Use Case   | Simple chatbots, RAG apps, tool usage                     | Multi-step workflows, agents with memory, conditional paths.            |
| State Handling  | Stateless or partially stateful                           | Fully stateful; remembers and transitions based on logic.              |
| Example Use     | "Book a flight" using a flight API                        | "Plan a vacation" (ask budget -> choose flights -> book hotel -> loop if error) |
| When to use     | Use LangGraph when you want structured workflows with some autonomy, state, memory, or conditional logic. | Use LangChain when building simpler, reactive agents or tool-chaining logic with more LLM-driven decision making.|

### Create a graph using Langgraph

```python
class SomeState(TypeDict):
    attribute1: float
    attribute2: int
    attribute3: str

def node_function1(state: SomeState) -> SomeState:
    # some operation on state
    return state

def node_function2(state: SomeState) -> SomeState:
    # some operation on state
    return state

from langgraph.graph import StateGraph, START, END

builder = StateGraph(<SomeState>) # Replace with your state type

builder.add_node("<node-name1>", <node_function1>)
builder.add_node("<node-name2>", <node_function2>)

builder.add_edge(START, "<node-name1>")
builder.add_edge("<node-name1>", "<node-name2>")
builder.add_edge("<node-name2>", END)

graph = builder.compile()
````

### Show the graph we just built

```python
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
```

### Invoke the graph
```python
graph.invoke(<pass-your-initial-state>) # Example {"amount_usd" : 1000} and then from state variable i can get this value state["amount_usd"]
```

### Create Graph using Langgraph with condition

```python
class SomeState(TypeDict):
    attribute1: float
    attribute2: int
    attribute3: str

def node_function1(state: SomeState) -> SomeState:
    # some operation on state
    return state

def node_function2(state: SomeState) -> SomeState:
    # some operation on state
    return state

from langgraph.graph import StateGraph, START, END

builder = StateGraph(<SomeState>) # Replace with your state type

builder.add_node("<node-name1>", <node_function1>)
builder.add_node("<node-name2>", <node_function2>)

builder.add_edge(START, "<node-name1>")
builder.add_conditional_edge(
    "<condition-defined-function>", 
    <conditional_edge>, 
    {
        "condition 1" : "<node-name1>",
        "condition 2" : "<node-name2>"
    }
)
builder.add_edge("<node-name1>", "<node-name2>")
builder.add_edge("<node-name2>", END)

graph = builder.compile()
````

### Show the graph we just built

```python
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
```

### Invoke the graph
```python
graph.invoke(<pass-your-initial-state>) # Example {"amount_usd" : 1000} and then from state variable i can get this value state["amount_usd"] also you can pass other argument also like {"amount_usd" : 1000, "currency": "INR"}
```


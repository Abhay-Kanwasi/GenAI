if __name__ == '__main__':
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    text = """
        Agentic AI refers to an advanced type of artificial intelligence that can autonomously make decisions, plan, and act to achieve goals with minimal human intervention. Unlike traditional AI that primarily reacts to prompts, agentic AI is proactive and can learn, adapt, and execute complex, multi-step tasks independently. These systems often use a combination of AI models to reason, interact with tools, and achieve specific business or user outcomes
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0
    )

    chunks = splitter.split_text(text)

    print(f'Chunks {chunks}\nLength of chunks is {len(chunks)}')
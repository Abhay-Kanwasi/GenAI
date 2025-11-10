if __name__ == '__main__':
    from langchain.text_splitter import CharacterTextSplitter

    # Text based
    text = """
        In order to perform a rigorous study of computation, computer scientists work with a mathematical abstraction of computers called a model of computation. There are several models in use, but the most commonly examined is the Turing machine.[2] Computer scientists study the Turing machine because it is simple to formulate, can be analyzed and used to prove results, and because it represents what many consider the most powerful possible "reasonable" model of computation (see Church–Turing thesis).[3] It might seem that the potentially infinite memory capacity is an unrealizable attribute, but any decidable problem[4] solved by a Turing machine will always require only a finite amount of memory. So in principle, any problem that can be solved (decided) by a Turing machine can be solved by a computer that has a finite amount of memory. 
    """

    splitter = CharacterTextSplitter(
        chunk_size=120,
        chunk_overlap=0,
        separator='',
    )

    print(f'Text based {splitter.split_text(text)}')

    # Document based
    from langchain.document_loaders import PyPDFLoader

    loader = PyPDFLoader('dl-curriculum.pdf')

    docs = loader.load()

    print(splitter.split_documents(docs)[0].page_content)





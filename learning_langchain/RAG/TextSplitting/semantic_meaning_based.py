if __name__ == '__main__':
    from langchain_openai import OpenAIEmbeddings
    from langchain_experimental.text_splitter import SemanticChunker
    from dotenv import load_dotenv

    sample = """
        The desert wind carved strange patterns into the dunes overnight, leaving behind ripples that looked almost like the surface of an ocean frozen in time, and travelers who passed through the region often wondered how something so barren could appear so alive, as if the sand itself were breathing. A violinist in Vienna once performed for an audience of cats, and though the animals did not clap or cheer, they tilted their heads, flicked their tails, and seemed to listen with a kind of curiosity that no human critic could ever replicate, making the performance both absurd and strangely profound, a reminder that art does not always need applause to matter. Astronauts often describe the smell of space as metallic and burnt, a scent that clings to their suits after a spacewalk, and though it cannot be inhaled directly in the vacuum, the lingering odor inside the spacecraft is said to resemble hot metal or seared steak.
    """
    
    text_splitter = SemanticChunker(
        OpenAIEmbeddings(),
        breakpoint_threshold_type="standard_deviation",
        breakpoint_threshold_amount=1
    )
    
    docs = text_splitter.create_document([sample])
    print(f'Chunks are : {docs}\nLength of chunks are : {len(docs)}.')
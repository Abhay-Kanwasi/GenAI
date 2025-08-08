from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Cognitive dissonance occurs when a person's beliefs and behaviors are inconsistent, causing psychological discomfort.",
    "Maslow's hierarchy of needs suggests humans are motivated by physiological, safety, love/belonging, esteem, and self-actualization needs.",
    "The placebo effect is when a person experiences a perceived improvement in condition due to the belief in a treatment, even if it has no active ingredient.",
    "Classical conditioning, demonstrated by Pavlov, occurs when a neutral stimulus becomes associated with a meaningful stimulus.",
    "Operant conditioning, studied by Skinner, involves learning through rewards and punishments.",
    "Confirmation bias leads individuals to seek and interpret information in ways that confirm their preexisting beliefs.",
    "The bystander effect describes the tendency of individuals to be less likely to help when others are present.",
    "Neuroplasticity refers to the brain's ability to reorganize itself by forming new neural connections.",
    "Emotional intelligence involves the ability to recognize, understand, and manage one's own emotions and the emotions of others.",
    "The Stroop effect demonstrates interference in reaction time when the brain processes conflicting information."
]

user_query = "Tell me about Cognitive dissonance ?"

documents_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(user_query)

similarity_scores = cosine_similarity([query_embedding], [documents_embedding])[0]  # both parameters must be a 2D list

index, similarity_score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1][-1])
"""we have to sort it without ruining the order so first enumerate, so we know the order of embedding according to  
document index and make a list, then we can sort that list based on similarity score, and it will come into ascending 
order now most similar will go into last so we will only extract that out."""

print(f'Output: {documents[index]}, similarity score: {similarity_score}')
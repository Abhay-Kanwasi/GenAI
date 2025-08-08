import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# By default
os.environ['HF_HOME'] = 'D:/huggingface'  # By default, hugging face related files goes to home or C drive but we can
# override it like this.


llm = HuggingFacePipeline.from_model_id(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

user_input = "Generate a blog about Langchain"

llm_output = model.invoke(user_input)

print(llm_output)

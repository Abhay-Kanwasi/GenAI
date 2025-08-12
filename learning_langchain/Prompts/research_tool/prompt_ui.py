import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatOpenAI()
st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraph)", "Medium (3-5 paragraph)", "Long (detailed explanation)"])

# Template
template = load_prompt('template.json')

# Fill the placeholder
# user_prompt_with_template = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input,
# })
#
# if st.button("Summarize"):
#     result = model.invoke(user_prompt_with_template)
#     st.write(result.content)

# But if we use chain we can avoid calling invoke 2 times
if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })
    st.write(result.content)
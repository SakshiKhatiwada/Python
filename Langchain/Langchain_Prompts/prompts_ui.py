from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool Model")

# user_input = st.text_input("Enter your prompt")
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention is All You Need",
        "BERT: Pre-training of Deep Bidirectional  Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# template
# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematcal Details:
#     - Include relevant mathematical equations if present in the paper
#     - Explain the mathematical concepts using simple, intuitive code snippets where applicabe.

# 2. Analogies:
#     - Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing.
# """,
# input_variables = ["paper_input", "style_input", "length_input"],
# validate_template = True # validates if all the placeholder variable names are in the variable input_variables
# )

template = load_prompt('Langchain/Langchain_Prompts/template.json')

# fill the placeholder
# prompt = template.invoke(
#     {
#         "paper_input": paper_input,
#         "style_input": style_input,
#         "length_input": length_input,
#     }
# ) # making a chain instead of this code, to invoke only one time
 
if st.button("Summarize"):
    # # result = model.invoke(user_input)
    # st.write(result.content)
    # st.write("haha")
    # result = model.invoke(prompt)
    # ---------------------
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })
    
    st.write(result.content)

# to run: streamlit run filename

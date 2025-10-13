from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()



llm1 = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task='text-generation'
)

llm2 = HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
    task='text-generation'
)

llm3 = HuggingFaceEndpoint(
    repo_id='moonshotai/Kimi-K2-Instruct-0905',
    task='text-generation'
)

llm4 = HuggingFaceEndpoint(
    repo_id='Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1',
    task='text-generation'
)
llm5 = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Next-80B-A3B-Instruct',
    task='text-generation'
)

query = """You are a compassionate and knowledgeable Mental Health Assistant 
    Your role is to help the user reflect, understand, and take small, practical steps toward better emotional and mental well-being.
    Cite your sources in parentheses like (Source [1]) when you use them.

    ---
    User's Query:
    I just can’t stop overthinking everything. My mind never shuts off.I prefer very short answers, empathetic and non-judgemental.
  
    ---
    ### Your Task:
    1. Understand the user's underlying concern and emotional tone.  
    2. Provide an answer that is:
    - **Empathetic:** Show understanding, warmth, and no judgment.
    - **Psychologically informed:** Use science-backed reasoning when possible.
    - **Action-oriented:** Offer 1–3 small, realistic next steps or insights.
    - **Concise and natural:** Write as if you’re talking gently to the user, not lecturing.
    3. If the information is insufficient, gently acknowledge that, and suggest where the user might explore further or what question to reflect on next.
    ### Format:
    - Begin with a short validating statement (e.g., “It’s okay to feel this way…” or “That’s a meaningful question.”).
    - Then give your main insight or explanation.
    - End with one small actionable takeaway or reflection prompt.
    Respond in a friendly, calm, and encouraging tone.,
"""

model1 = ChatHuggingFace(llm=llm1)
result1 = model1.invoke(query)
model2 = ChatHuggingFace(llm=llm2)
result2 = model2.invoke(query)
model3 = ChatHuggingFace(llm=llm3)
result3 = model3.invoke(query)
# model4 = ChatHuggingFace(llm=llm4)
# result4 = model4.invoke(query)
model5 = ChatHuggingFace(llm=llm5)
result5 = model5.invoke(query)

print('\n---------------------Model 1: Deepseek ------------------\n\n: ',result1.content)
print('\n---------------------Model 2: Meta ------------------\n\n: ',result2.content)
print('\n---------------------Model 3: Moonshotai ------------------\n\n: ',result3.content)
# print('\n---------------------Model 4: Josiefied-Qwen3...------------------\n\n: ',result4.content)
print('\n---------------------Model 5: Qwen-----------------\n\n: ',result5.content)


# ----------------- Extras

# llm1 = HuggingFaceEndpoint(
#     repo_id='mistralai/Mistral-7B-Instruct-v0.3',
#     task='text-generation'
# )
# ---------------------------

# llm3 = HuggingFaceEndpoint(
#     repo_id='meta-llama/Llama-2-7b-chat-hf',
#     task='text-generation'
# ) # gated access


# llm3 = HuggingFaceEndpoint(
#     repo_id='Salesforce/CoDA-v0-Instruct',
#     task='text-generation'
# )
# llm3 = HuggingFaceEndpoint(
#     repo_id='nvidia/NVIDIA-Nemotron-Nano-9B-v2',
#     task='text-generation'
# ) # gated access

# llm3 = HuggingFaceEndpoint(
#     repo_id='ai21labs/AI21-Jamba-Reasoning-3B',
#     task='text-generation'
# )

# llm4 = HuggingFaceEndpoint(
#     repo_id='google/gemma-3n-E4B-it-litert-lm',
#     task='text-generation'
# )
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='text-generation'
)

llm2 = HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
    task='text-generation'
)

# llm3 = HuggingFaceEndpoint(
#     repo_id='Salesforce/CoDA-v0-Instruct',
#     task='text-generation'
# )

llm4 = HuggingFaceEndpoint(
    repo_id='Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1',
    task='text-generation'
)

# llm5 = HuggingFaceEndpoint(
#     repo_id='moonshotai/Kimi-K2-Instruct-0905',
#     task='text-generation'
# )
# ---------------------------

# llm3 = HuggingFaceEndpoint(
#     repo_id='meta-llama/Llama-2-7b-chat-hf',
#     task='text-generation'
# ) # gated access

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

query = "Explain astrology for kids"

model1 = ChatHuggingFace(llm=llm1)
result1 = model1.invoke(query)
model2 = ChatHuggingFace(llm=llm2)
result2 = model2.invoke(query)
# model3 = ChatHuggingFace(llm=llm3)
# result3 = model3.invoke(query)
model4 = ChatHuggingFace(llm=llm4)
result4 = model4.invoke(query)
# model5 = ChatHuggingFace(llm=llm5)
# result5 = model5.invoke(query)

print('\n---------------------Model 1: Mistral ------------------\n\n: ',result1.content)
print('\n---------------------Model 2: Meta ------------------\n\n: ',result2.content)
# print('\n---------------------Model 3: SalesForce ------------------\n\n: ',result3.content)
print('\n---------------------Model 4: Josiefied-Quen3-8B...------------------\n\n: ',result4.content)
# print('\n---------------------Model 5 ------------------\n\n: ',result5.content)

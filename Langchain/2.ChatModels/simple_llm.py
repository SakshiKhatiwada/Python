from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()



llm1 = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task='text-generation'
)

model1 = ChatHuggingFace(llm=llm1)
result1 = model1.invoke("I am feeling so anxious")
print('result',result1.content)

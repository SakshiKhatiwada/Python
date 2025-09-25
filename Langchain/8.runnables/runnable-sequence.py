from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="Tell me a joke about {topic}", input_variables=["topic"]
)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)
result = chain.invoke({"topic": "AI"})
print(result)
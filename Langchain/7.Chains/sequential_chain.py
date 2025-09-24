from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# prompt 1
report_prompt = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

summary_prompt = PromptTemplate(
    template= "Based on the report `{report}`, generate a 5 line summary",
    input_variables= ['report']
)

chain = report_prompt | model | parser | summary_prompt | model | parser
result = chain.invoke({"topic": "Internship in Kathmandu"})
print(result)

print(chain.get_graph().draw_ascii())


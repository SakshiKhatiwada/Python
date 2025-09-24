from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

# 1st prompt
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt => summary
template2 = PromptTemplate(
    template='write a 5 line summary of the following text. /n {text}',
    input_variables=['text']
)

# prompt1 = template1.format() # can do both
prompt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

final_result = model.invoke(prompt2)

print(result.content)
print(final_result.content)
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Give me the name, age, address and marital status of a fictional person\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Normally,
# prompt = template1.format()

# print('prompt: ', prompt)

# result = model.invoke(prompt)
# print(result)

# op = parser.parse(result.content)

# using Chains
chain = template1 | model | parser
op = chain.invoke({}) # while invoking, we need to send something anything, so empty dict

# same for both
print("output: ", op)
print("type: ", type(op))
print(op['name'])

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(description="Give the sentiment of the feedback")
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative:\n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# print("prompt1: ", prompt1)
# result = classifier_chain.invoke({"feedback": "This is a great smartphone"})
# print(result)
# print(result.sentiment)
# print("type: ", type(result))


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback: \n{feedback}',
    input_variables=['feedback']  
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback: \n{feedback}',
    input_variables=['feedback']  
)

# SYNTAX
# branch_chain = RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default chain
# )

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', prompt3 | model | parser ),
    RunnableLambda(lambda x: "could not find sentiment") # NOTE: It converts lambda function into Runnable and then we can use it as chain. This is LangChain's universal chain
)

chain = classifier_chain | branch_chain
print(chain.invoke({"feedback": "I absolutely love this laptop"}))
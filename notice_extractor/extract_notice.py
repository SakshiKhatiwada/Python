import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser

load_dotenv()

llm = HuggingFaceEndpoint(
    model_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=256,
    do_sample=False,
    temperature=0.7,
    top_p=0.9,
)

model = ChatHuggingFace(llm=llm)


class Notice(BaseModel):
    title: str = Field(description="Title of the Notice")
    description: str = Field(description="Description of the Notice")


parser = PydanticOutputParser(pydantic_object=Notice)

template = PromptTemplate(
    template="""
    I am providing you scraped page contents from websites. Extract notices from them and return only in JSON format
    {format_instruction}
    
    Context:
    {context}
    """,
    input_variables=["context"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser

# converting scraped docs to text
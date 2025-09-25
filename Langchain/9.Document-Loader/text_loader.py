from langchain_community.document_loaders import TextLoader

# from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("Langchain/9.Document-Loader/poem.txt", encoding="utf-8")

docs = loader.load()  # simply loads the document in the memory

# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print('type of docs[0]: ', type(docs[0])) # <class 'langchain_core.documents.base.Document'>

# model = ChatOpenAI()
llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation")

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Write a summary for the following poem -\n {poem}",
    input_variables=["poem"],
)
parser = StrOutputParser()

chain = prompt | model | parser
# result = chain.invoke({"poem": docs[0].page_content})
result = chain.invoke(docs[0].page_content)
print(result)

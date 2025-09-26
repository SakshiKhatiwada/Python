from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader

# from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7w4hn-a/p/itm2ea42dec44bca?pid=COMH64PYZU4ZZR79&lid=LSTCOMH64PYZU4ZZR79AHLYXY&marketplace=FLIPKART&q=apple+macbook+air&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=en_gnjVW-xrSuR_nhlq_Epyl2slf_GNPVIFj9Y_uUkDg8yGh8gyO1y9mbXQu1tjQ2uh5eYBMdXqba4Rs2LTBeQQlPUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=62q5y3kybk0000001758854357945&qH=715ebb8705dbcf37"

# model = ChatOpenAI()

llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation")
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Answer the following Question: \n {question} from the following text: \n{text}",
    input_variables=["question", "text"],
)
parser = StrOutputParser()

loader = WebBaseLoader(url)  # we can pass many URLs
docs = loader.load()


# print(docs)
# print(len(docs))
# print(docs[0].page_content)

chain = prompt | model | parser

chain.invoke({'question':"what is the battery capacity of this product? How many hours will it will last under continuous use?", 'text': docs[0].page_content})

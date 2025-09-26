from langchain.text_splitter import CharacterTextSplitter  # length-based
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/home/sakshi-khatiwada/Desktop/chatbot-assistant-for-adhd.pdf")

# text = """One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.

# Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." They meant well, but this is rarely true. If your product is only half as good as your competitor's, you don't get half as many customers. You get no customers, and you go out of business.
# """

# splitter = CharacterTextSplitter(
#     chunk_size=10,
#     chunk_overlap = 0,
#     separator=''
# )

# result = splitter.split_text(text)

# docs = loader.load()
# splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")

# result = splitter.split_documents(docs)
# print(result[0])
# print(len(result))  # 2997 for size 10, 301 for 100

# SECTION 
# from langchain.text_splitter import (
#     RecursiveCharacterTextSplitter,
# )  # text-structured-based

# splitter2 = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=0)

# text = """One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.

# Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." """

# chunks = splitter2.split_text(text)
# print(len(chunks))
# print(chunks)

# SECTION

# from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

# text = """
# class Student:
#     def __init__(self,name):
#         self.name = name
        
#     def get_name(self):
#     return self.name
    
# student = Student("Sakshi")
# print(student.get_name())"""


# splitter3 = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON,
#     chunk_size=100,
#     chunk_overlap=0
# )

# chunks = splitter3.split_text(text)
# print(len(chunks))
# print(chunks[0])


# SECTION

from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

text_splitter = SemanticChunker(
    HuggingFaceEmbeddings(),
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

sample = """Farmer helps to harvest crops. IPL is the india's biggest cricket league.

Terrorism is a big danger. To fight terrorism, we need strong laws.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)
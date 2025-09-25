# most used document loader
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/home/sakshi-khatiwada/Desktop/chatbot-assistant-for-adhd.pdf')

docs = loader.load()
print(len(docs))
print(docs[0].metadata)
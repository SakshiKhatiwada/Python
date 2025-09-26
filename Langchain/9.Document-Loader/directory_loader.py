from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='/home/sakshi-khatiwada/Desktop/E-Commerce',
    glob='*.pdf',
    loader_cls= PyPDFLoader
)

docs = loader.load()
# print(len(docs))
print(docs[0])
# print(docs[0])
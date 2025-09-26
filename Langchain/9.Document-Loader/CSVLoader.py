from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='/home/sakshi-khatiwada/Desktop/My Repos/Assignments/Coding-Assignments/movies_metadata.csv')

docs = loader.load()
# docs = loader.lazy_load() # gives generator and we have to loop over it

print(len(docs))
print(docs[0])

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from sklearn.metrics.pairwise import cosine_similarity


# embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
# print(embedding_model.embed_query("test"))
embedding = HuggingFaceEmbeddings(model_name="google/embeddinggemma-300m") 
# print(embedding_model.embed_query("test"))


document = [
    'Virat Kohli is an Indian Cricketer known for his aggressive batting and leadership.',
    "Sandip Lamichhane is a Nepali cricketer winning everone's heart.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Ms Dhoni is a former Indian captain, famous for his calm Demeanor and finishing skills.",
    "Ms Dhoni's wife name is Sakshi, which is my name too."
]

query = 'Tell me about Sakshi'

doc_embeddings = embedding.embed_documents(document)
query_embeddings = embedding.embed_query(query)

print(cosine_similarity([query_embeddings], doc_embeddings))
from langchain_huggingface import HuggingFaceEmbeddings

# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embedding = HuggingFaceEmbeddings(model_name="google/embeddinggemma-300m")

text = 'Kathmandu is the capital of Nepal'

vector = embedding.embed_query(text)
print('vector',vector)
print('vector in str', str(vector))
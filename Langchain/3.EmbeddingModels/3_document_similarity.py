from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# I don't have the API key, this is just practice of syntax to do
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

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

print(cosine_similarity([query_embeddings], doc_embeddings)) #NOTE cosine_similarity need both arguments as 2D list
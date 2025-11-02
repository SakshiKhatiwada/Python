import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# object creation
ps = PorterStemmer()

# loading
tfidf = pickle.load(open('Spam-Filter/vectorizer.pkl', 'rb'))
model = pickle.load(open('Spam-Filter/model.pkl', 'rb'))

# function definition
def transform_text(text):
    """
    Preprocess the text and returns string
    """
    
    tokens_list = nltk.word_tokenize(text.lower())
    
    processed = []
    
    for word in tokens_list:
        if word.isalnum() and word not in stopwords.words('english') and word not in string.punctuation:
            processed.append(ps.stem(word))
    
    return " ".join(processed)

# UI building

st.title("Message Spam Classification")
input_message = st.text_area("Enter your message:")

if st.button("Predict"):
    # 1. Preprocess
    transformed_text = transform_text(input_message)
    print('transformed text: ', [transform_text])
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_text])
    # 3. Predict
    result = model.predict(vector_input)[0]
    print('result: ', model.predict(vector_input))
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

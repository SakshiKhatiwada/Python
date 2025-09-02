from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation"
)
model = ChatHuggingFace(llm=llm)
chat_history = [SystemMessage(content='You are a helpful AI assistant')]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history) #INFO - Invoke function is flexible enough to take single message or a list
    chat_history.append(AIMessage(result.content))
    print("AI: ", result.content)
    
print(chat_history)

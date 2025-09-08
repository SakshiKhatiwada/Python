from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# chat_template = ChatPromptTemplate(
#     [
#         SystemMessage(content="You are a helpful {domain} expert"),
#         HumanMessage(content='Explain in simple terms, what is {topic}')
#     ]
# ) #INFO - This doesn't work

# chat_template = ChatPromptTemplate.from_messages( # works the same

chat_template = ChatPromptTemplate(
    [
        ('system', "You are a helpful {domain} expert"),
        ('human', "Explain in simpl terms, what is {topic}")
    ]
)

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})

print(prompt)
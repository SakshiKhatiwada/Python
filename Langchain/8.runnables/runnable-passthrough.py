from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='Explain this joke to me: {joke}',
    input_variables=['joke']
)

chain1 = RunnableSequence(prompt1, model, parser)
chain2 = RunnableParallel({
    'joke': RunnablePassthrough() ,
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(chain1, chain2)
result = final_chain.invoke({'topic': "AI"})
print('result:', result)
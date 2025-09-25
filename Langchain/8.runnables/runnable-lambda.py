from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}", input_variables=["topic"]
)

chain1 = RunnableSequence(prompt1, model, parser)
chain2 = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count":RunnableLambda(lambda x: len(x.split())) # split(" ")) same thing
    }
)

final_chain = chain1 | chain2

result = final_chain.invoke({'topic': "banana"})
print('joke: ', result['joke'])
# print('word_count: ', result['word_count']) 

final_result = """{}\n word count: {}""".format(result['joke'], result['word_count']) # better formatting
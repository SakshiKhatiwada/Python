from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.8,
        max_new_tokens=150
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Nepal?")
print(result.content)
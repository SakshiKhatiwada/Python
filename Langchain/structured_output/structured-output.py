# using with_structured_output() => and provide data format

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from langchain_openai import ChatOpenAI

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.3",
#     task=""
# )

# model = ChatHuggingFace(llm=llm)
model = ChatOpenAI()

# schema for new data format
class Review(TypedDict): #NOTE this is just for Representation, it's not validation 
    summary: str # Simple TypedDict
    sentiment: Annotated[Literal['Positive', 'Negative'], 'sentiment of the review as either negative, positive or neutral'] # Annotated TypedDict: no guessing game, give llm the complete information
    # for more lengthy review
    key_themes: Annotated[list[str], "Write all the key themes discussed in the review in a list"]
    pros: Annotated[Optional[list[str]], "list all the advantages"]
    cons: Annotated[Optional[list[str]], "list all the disadvantages unless explicitly mentioned"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(Review) # won't work here, it's OpenAI-style structured output support

result = structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")

print("result", result)
print("type: ", type(result))

# ---------------

# prompt = (
#     "Return a JSON object with keys 'Summary' and 'Sentiment'."
#     "Text: The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
# )

# prompt = (
#     "Summarize and provide sentiment of the review"
#     "Respong ONLY in valid JSON object with keys 'Summary' and 'Sentiment'."
#     "Text: The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
# )

# response = model.invoke(prompt)

# print("response: ", response)
# print("type: ", type(response.content))
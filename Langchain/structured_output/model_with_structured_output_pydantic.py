# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, TypedDict, Annotated, Literal

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.3", task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)
model = OpenAI()

class Review(BaseModel):
    key_themes: list[str] = Field(description="themes of the review")
    summary: str = Field(description="a brief summary of the review")
    sentiment: Literal["Pos", "Neg"] = Field(
        description="Return the sentiment of the review, either pos or neg"
    )
    pros: Optional[list[str]] = Field(
        default=None, description="Write down all the pros inside a list"
    )  # Giving default value is must Optional
    cons: Optional[list[str]] = Field(
        default=None, description="Write down all the cons inside a list"
    )
    name: Optional[str] = Field(default=None, description="name of the author")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")

print("result", result)
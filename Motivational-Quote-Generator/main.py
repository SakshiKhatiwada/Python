from fastapi import FastAPI
from typing import Union
# from quotes import quotes_dict
import json

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": 'World'}

@app.get("/quotes/{quote_id}")
def show_types(quote_id: int):
    if quote_id < 10 and quote_id>0:
        quote = quotes_dict[str(quote_id)]
        return {"Quote of the Day": quote }
    else:
        return {"Error", "Quotes not available for that id"}
    
@app.post("/")
def update_quote(quote_id:int, new_quote: Union[str, None]):
    if quote_id < 10 and quote_id>0:
        with open("quotes.py") as f:
            quotes_dict = json.load(f)
            quotes_dict[str(quote_id)]= new_quote
            # json.dump()
        return {"message": "Quote Updation Successful"}
    return {"message": "Quote didn't update."}
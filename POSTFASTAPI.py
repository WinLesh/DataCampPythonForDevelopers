#POST operation in action
#You've been asked to create an API endpoint that accepts a name parameter 
# and returns a message saying "We have name". To accomplish this, 
# create a Pydantic model for Item and root endpoint (/) that serves HTTP POST operations.
#  The endpoint should accept the Item model as input and respond with a message including Item.name.
#You can't run the FastAPI server directly with "Run this file" 
# - see the instructions for how to run the server and test your code from the terminal.
#Define pydantic model Item so that parameter name can be passed into the POST body.
#Run the live server in the terminal: fastapi dev main.py

#    Open a new terminal (top-right of terminal) and test your code with the following command:

#curl -X POST \
  #-H 'Content-Type: application/json' \
  #-d '{"name": "bananas"}' \
  #http://localhost:8000

from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

app = FastAPI()


@app.post("/")
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}
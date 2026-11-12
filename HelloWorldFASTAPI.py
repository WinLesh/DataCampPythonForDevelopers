#Let's build your first GET endpoint! 
# You can't run the FastAPI server directly with "Run this file" 
# - see the instructions for how to run and stop the server from the terminal.
#Instructions
# Import FastAPI and instantiate the app server.
# Run the live server in the terminal: fastapi dev main.py.
#Open a new terminal (top-right of terminal)
# Terminal with arrow pointing to the "new terminal" button on top right.
#Test your code with the following command

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
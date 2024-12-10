# main.py
from fastapi import FastAPI

# uvicorn is the bare-bones web server that FastAPI runs on.
import uvicorn

app = FastAPI()

# in Python @app syntax is commonly seen in web frameworks like FastAPI.
# when setting up it is part of the decoretor syntax.
# app = FastAPI() variable app becomes an instance of the FastAPI class


@app.get("/")
def root_controller():
    return {"status": "healthy"}


# __name__ is a built-in variable
# that represents the name of the current module:
# if the Python script is executed directly the value of __name__ is "__main__"
# when the module is imported __name__ is set to the module's name (file name)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

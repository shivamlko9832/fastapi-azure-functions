from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Azure Functions! 🚀"}

@app.get("/sample")
def sample():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
def get_name(name: str):
    return {"message": f"Hello, {name}!"}
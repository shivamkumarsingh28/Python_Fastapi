from fastapi import FastAPI

app = FastAPI()

@app.get("/saeeam")
def root():
   return {"message": "Hello World"}
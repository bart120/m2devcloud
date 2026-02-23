from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API fonctionne"}

# pip install fastapi uvicorn[standard] 
 #   azure-cosmos pydantic-settings python-dotenv


 # python -m uvicorn app.main:app --reload
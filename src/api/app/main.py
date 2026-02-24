from fastapi import FastAPI
from .routes_jobs import router as jobs_router

app = FastAPI(title="Doc processing API")

app.include_router(jobs_router)


@app.get("/health")
def health():
    return {"status":"ok"}




#@app.get("/")
#def root():
#    return {"message": "API fonctionne"}

# pip install fastapi uvicorn[standard] azure-cosmos pydantic-settings python-dotenv


 # python -m uvicorn app.main:app --reload
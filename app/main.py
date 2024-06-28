from fastapi import FastAPI
from app.api import auth, emotions, journals

app = FastAPI()

app.include_router(auth.router)
app.include_router(emotions.router)
app.include_router(journals.router)

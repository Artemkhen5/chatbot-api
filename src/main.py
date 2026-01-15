from dotenv import load_dotenv
from fastapi import FastAPI

from src.api import endpoints

load_dotenv()
app = FastAPI()
app.include_router(endpoints.router)

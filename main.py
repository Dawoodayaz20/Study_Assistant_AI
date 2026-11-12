from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from dotenv import load_dotenv, find_dotenv
import os

# load_dotenv(find_dotenv())
app = FastAPI()
# request_origin = os.getenv("request_origin")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def check_api():
    return {
        "success": "true", 
        "message": "Hello World"
        }



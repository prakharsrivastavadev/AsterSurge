"""
AsterSurge API

Version: 0.3.0
"""

from fastapi import FastAPI
from pydantic import BaseModel

from .agent import Agent
from .config import Config
from .factory import ProviderFactory

app = FastAPI(
    title="AsterSurge",
    version=Config.VERSION,
)

agent = Agent(
    provider=Config.PROVIDER,
    model=Config.MODEL,
)


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "name": Config.APP_NAME,
        "version": Config.VERSION,
        "provider": Config.PROVIDER,
        "model": Config.MODEL,
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }


@app.get("/version")
def version():
    return {
        "version": Config.VERSION,
    }


@app.get("/providers")
def providers():
    return {
        "providers": ProviderFactory.available(),
    }


@app.get("/config")
def configuration():
    return Config.as_dict()


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = agent.chat(request.prompt)
    return ChatResponse(response=response)

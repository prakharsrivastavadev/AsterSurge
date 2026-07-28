"""
AsterSurge API

Version: 0.2.0
"""

from fastapi import FastAPI
from pydantic import BaseModel

from .agent import Agent

app = FastAPI(
    title="AsterSurge",
    version="0.2.0",
)

agent = Agent()


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "name": "AsterSurge",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = agent.run(request.prompt)

    output = ""

    if isinstance(result, dict):
        if "results" in result:
            output = "\n".join(
                str(item.get("output", ""))
                for item in result["results"]
            )
        else:
            output = str(result)
    else:
        output = str(result)

    return ChatResponse(response=output)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from AIClient import AIClient
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Chat Server")

# CORS to allow Reflex front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-reflex-app.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: Optional[str]
    citations: Optional[List[str]]

# Initialize AIClient
api_key = os.getenv("XAI_API_KEY")
if not api_key:
    raise RuntimeError("XAI_API_KEY environment variable not set. Set it in .env with your key from https://x.ai/api")

client = AIClient(api_key)

@app.get("/api/greeting", response_model=ChatResponse)
async def get_greeting():
    response, citations = client.generate_text("Give me a greeting")
    if response:
        return {"response": response, "citations": citations}
    raise HTTPException(status_code=500, detail="Failed to generate greeting")

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    prompt = request.prompt
    if "bye" in prompt.lower():
        response, citations = client.generate_text("Give me a farewell sign off")
    else:
        response, citations = client.generate_text(prompt)
    
    if response:
        return {"response": response, "citations": citations}
    raise HTTPException(status_code=500, detail="Failed to generate response")

@app.get("/api/farewell", response_model=ChatResponse)
async def get_farewell():
    response, citations = client.generate_text("Give me a farewell sign off")
    if response:
        return {"response": response, "citations": citations}
    raise HTTPException(status_code=500, detail="Failed to generate farewell")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
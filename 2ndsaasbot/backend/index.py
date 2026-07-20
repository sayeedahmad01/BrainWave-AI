from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {
        "status": "healthy",
        "service": "FastAPI Chatbot Backend"
    }

@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        user_message = request.message

        return {
            "response": f"You said: {user_message}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.emotion import detect_emotion
from app.services.response_gen import generate_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    emotion = detect_emotion(req.message)
    reply = generate_response(emotion, req.message)
    return ChatResponse(emotion=emotion, response=reply)

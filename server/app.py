from fastapi import FastAPI
from pydantic import BaseModel
from classifier import classify_call
from sheets import append_to_sheet


app= FastAPI()

class CallPayload(BaseModel):
    phone: str
    transcript: str


@app.post("/voice-webhook")
def voice_webhook(payload: CallPayload):
    result = classify_call(payload.transcript)

    append_to_sheet({
        "phone": payload.phone,
        "intent": result['intent'],
        "urgency": result['urgency'],
        "summary": result['summary']
        })
    
    return {
        'success': True,
        'classification': result
    }
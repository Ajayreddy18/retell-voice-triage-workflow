def classify_call(transcript:str):
    text = transcript.lower()

    if 'buy' in text or 'price' in text:
        intent = 'sales'

    elif 'issue' in text or 'problem' in text:
        intent = 'support'

    else:
        intent = 'general'

    urgency = 'high' if 'urgent' in text else 'normal' 

    
    return {
        "intent": intent,
        "urgency": urgency,
        "summary": transcript[:120]
    }
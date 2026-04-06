from fastapi import FastAPI
app = FastAPI()

@app.get("/tools")

def list_tools():
    return {
        "tools": [
            {
                "name": "create_call_agent",
                "description": "Creates a Retell-style call workflow"
        
          }
        ]
    }

@app.post("/create_call_agent")

def create_call_agent(payload: dict):
    return {
        'status': 'created',
        'agent_name': payload.get('name', 'sales-agent')
    }
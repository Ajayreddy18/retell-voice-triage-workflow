# Retell Voice Triage Workflow

A production-style **voice AI support triage pipeline** that converts call transcripts into structured CRM actions using **Retell, n8n, FastAPI, and Google Sheets**.

This project demonstrates how to build an **event-driven AI workflow** for startups that need fast customer support routing, lead qualification, and escalation logic.

---

##  What it does

When a voice transcript is received from a Retell AI call agent:

1. **Retell sends transcript data** to an n8n webhook
2. **n8n triggers the workflow**
3. **FastAPI backend classifies the call**

   * intent detection
   * urgency detection
   * transcript summarization
4. **Results are stored in Google Sheets CRM**
5. The workflow returns a **clean JSON response** for downstream automation

---

##  Example Use Cases

* Voice support ticket triage
* Urgent escalation detection
* AI receptionist workflows
* Sales lead qualification
* Post-call CRM enrichment
* Customer success routing

---

##  System Architecture

```text
Retell Voice Agent
      ↓
Webhook Trigger (n8n)
      ↓
HTTP Request Node
      ↓
FastAPI Backend
      ↓
Intent + Urgency Classifier
      ↓
Google Sheets CRM
      ↓
JSON Response
```

---

##  Tech Stack

* **Retell AI** → voice transcript source
* **n8n** → workflow orchestration
* **FastAPI** → backend webhook + classifier API
* **Python** → classification logic
* **Google Sheets API** → lightweight CRM sink
* **gspread + service account** → Sheets integration

---

##  Project Structure

```text
retell-integration-proof/
│
├── server/
│   ├── app.py
│   ├── classifier.py
│   ├── sheets.py
│   ├── requirements.txt
│   └── .env.example
│
├── mcp-server/
│   ├── server.py
│   └── requirements.txt
│
├── n8n-node/
│   ├── RetellTrigger.node.ts
│   ├── package.json
│   └── tsconfig.json
│
├── workflows/
│   └── retell_voice_to_sheet.json
│
└── README.md
```

---

##  FastAPI Endpoint

### POST `/voice-webhook`

### Request

```json
{
  "phone": "+919999999999",
  "transcript": "urgent pricing issue please help"
}
```

### Response

```json
{
  "success": true,
  "classification": {
    "intent": "support",
    "urgency": "high",
    "summary": "urgent pricing issue please help"
  }
}
```

---

##  Local Setup

### 1) Clone repo

```bash
git clone <your-repo-url>
cd retell-voice-triage-workflow
```

### 2) Install backend deps

```bash
pip install fastapi uvicorn gspread google-auth
```

### 3) Start FastAPI

```bash
cd server
uvicorn app:app --reload
```

Open docs:

```text
http://127.0.0.1:8000/docs
```

### 4) Start n8n

```bash
n8n
```

Open:

```text
http://localhost:5678
```

### 5) Import workflow

Import `workflows/n8n-retell.json`

---

##  Why this project stands out



It showcases **real startup engineering skills**:

* rapid prototyping
* webhook integrations
* API schema validation
* event-driven orchestration
* AI classification workflows
* CRM persistence
* debugging auth + scopes
* production-style system thinking

This is highly relevant for:

* AI workflow engineering
* voice AI startups
* backend automation roles
* YC prototype rounds
* agent infrastructure teams

---



## 🔮 Future Upgrades

Planned production extensions:

* Slack escalation for high urgency
* email notifications
* ticket creation in HubSpot / Zendesk
* lead scoring
* multi-agent routing
* LLM-powered transcript enrichment
* sentiment analysis
* analytics dashboard

---



This project reflects my ability to:

* understand ambiguous workflow problems quickly
* ship a working MVP in hours
* debug multi-system integrations end-to-end
* convert AI workflows into business outcomes

If your team is building **voice AI, support automation, agent infrastructure, or workflow products**, this is exactly the type of system I can ship fast.

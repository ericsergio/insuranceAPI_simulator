from fastapi import FastAPI

app = FastAPI()

@app.get("/api/tasks")
def get_tasks():
    return {
        "queue": [
            {"claim_id": "CLM-2026-881A", "type": "Auto Liability", "status": "Pending Statement"},
            {"claim_id": "CLM-2026-904B", "type": "Property Damage", "status": "Review Estimate"}
        ]
    }

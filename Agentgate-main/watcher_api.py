from fastapi import FastAPI

app = FastAPI(title="AgentGate API")

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "AgentGate"
    }

@app.get("/health")
def health():
    return {
        "health": "ok"
    }
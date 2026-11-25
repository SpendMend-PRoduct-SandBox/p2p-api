from fastapi import FastAPI

app = FastAPI(title="p2p-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(title="Spell Caster")


@app.get("/health")
def health():
    return {"status": "ok"}

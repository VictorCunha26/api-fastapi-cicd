from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}


@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(title="CloudOps API", version="1.0.0")


@app.get("/")
def home():
    return {
        "mensagem": "Hello World - CloudOps Pipeline!",
        "status": "online",
        "versao": "1.0.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

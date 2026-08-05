app = FastAPI(
    title="Indian Weather & Cinema Agent",
    version="1.0",
    description="LangServe API for Indian Weather and Cinema Assistant"
)

add_routes(
    app,
    formatted_agent_chain,
    path="/agent"
)

@app.get("/")
def root():
    return {
        "message": "Indian Weather & Cinema Agent is running.",
        "docs": "/docs",
        "playground": "/agent/playground"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

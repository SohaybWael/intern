import uvicorn
from fastapi import FastAPI
from route import router
from config import settings

app = FastAPI(
    title="FastAPI Test APP",
    description="That is desc of our app"
)


@app.get('/')
def root():
    return modelX.getX()

app.include_router(router, tags=["User"], prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.DEBUG_MODE,
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT
        )

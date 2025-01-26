from fastapi import Depends, FastAPI
from .dependencies import get_api_key
from .routers import lab

app = FastAPI()

app.include_router(lab.router, prefix="/lab", tags=["lab"], dependencies=[Depends(get_api_key)])

@app.get("/")
async def root():
    return {"message": ":)"}

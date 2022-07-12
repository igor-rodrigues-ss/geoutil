from fastapi import FastAPI

from src.vector.urls import router as router_vector
from src.external.urls import router as router_external

from src.external.helper.client import client


app = FastAPI()


app.include_router(router_external, prefix="/external", tags=["External"])
app.include_router(router_vector, prefix="/vector", tags=["Vector"])


@app.on_event("shutdown")
async def shutdown_event():
    await client.aclose()

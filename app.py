from fastapi import FastAPI
import asyncio
from src.api.endpoints import router, background_task

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(background_task())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
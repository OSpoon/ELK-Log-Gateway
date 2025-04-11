import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.api.endpoints import router, background_task

app = FastAPI()
app.include_router(router)

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def root():
    return FileResponse("src/static/index.html")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(background_task())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
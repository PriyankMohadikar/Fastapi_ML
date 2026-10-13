from contextlib import asynccontextmanager
from fastapi import FastAPI
# from pydantic import BaseModel
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from routers.endpoints import router

# lecture 2 - pydantic class

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting lifespan")
    yield
    print("Stopping lifespan")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)



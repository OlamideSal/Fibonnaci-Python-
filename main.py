# app/main.py
from fastapi import FastAPI
from .utils import fibonacci
from .health import health_check
from pydantic import BaseModel
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis

app = FastAPI(title="Fibonacci Sequence API")

class FibonacciRequest(BaseModel):
    n: int

@app.on_event("startup")
async def startup():
    redis_client = redis.from_url("redis://localhost")
    await FastAPILimiter.init(redis_client)

@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    return {"n": n, "fibonacci": fibonacci(n)}

@app.post("/fibonacci")
async def post_fibonacci(request: FibonacciRequest):
    return {"n": request.n, "fibonacci": fibonacci(request.n)}

@app.get("/health")
async def health():
    return health_check()
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from products.views import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(products_router, prefix="/products", tags=["Products"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

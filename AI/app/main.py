from fastapi import FastAPI
from app.api.routes import router

# Initialize FastAPI app
app = FastAPI()

# Include API routes
app.include_router(router)

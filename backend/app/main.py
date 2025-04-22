import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.endpoints import code_generation, code_explanation, documentation, code_review
from app.core.config import settings

app = FastAPI(
    title="AI Code Assistant API",
    description="API for AI-powered code assistance using LLMs",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(code_generation.router, prefix="/api/generate", tags=["Code Generation"])
app.include_router(code_explanation.router, prefix="/api/explain", tags=["Code Explanation"])
app.include_router(documentation.router, prefix="/api/docs", tags=["Documentation"])
app.include_router(code_review.router, prefix="/api/review", tags=["Code Review"])

# Optional: Add vector DB router if implemented
from app.api.endpoints import vector_db
app.include_router(vector_db.router, prefix="/api/vector", tags=["Vector Database"])

@app.get("/")
async def root():
    return {"message": "Welcome to AI Code Assistant API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


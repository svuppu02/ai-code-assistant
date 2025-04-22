from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional, Any

from app.services.vector_db_service import VectorDBService

router = APIRouter()

class StoreCodeRequest(BaseModel):
    code: str
    language: str
    metadata: Optional[Dict[str, Any]] = None

class SearchCodeRequest(BaseModel):
    query: str
    language: Optional[str] = None
    n_results: Optional[int] = 5

class StoreCodeResponse(BaseModel):
    code_id: str

class SearchCodeResponse(BaseModel):
    results: List[Dict[str, Any]]

@router.post("/store", response_model=StoreCodeResponse)
async def store_code(request: StoreCodeRequest):
    """Store code in the vector database"""
    try:
        service = VectorDBService()
        code_id = await service.store_code(
            code=request.code,
            language=request.language,
            metadata=request.metadata
        )
        return StoreCodeResponse(code_id=code_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to store code: {str(e)}")

@router.post("/search", response_model=SearchCodeResponse)
async def search_code(request: SearchCodeRequest):
    """Search for similar code snippets"""
    try:
        service = VectorDBService()
        results = await service.search_similar_code(
            query=request.query,
            language=request.language,
            n_results=request.n_results
        )
        return SearchCodeResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
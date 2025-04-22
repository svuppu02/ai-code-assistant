from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional, Any

from app.services.code_review_service import CodeReviewService

router = APIRouter()

class CodeReviewRequest(BaseModel):
    code: str
    language: str
    quality_focus: Optional[bool] = True
    perf_focus: Optional[bool] = True
    security_focus: Optional[bool] = True
    style_focus: Optional[bool] = True
    additional_considerations: Optional[str] = ""
    temperature: Optional[float] = 0.3

class RefactoringRequest(BaseModel):
    code: str
    language: str
    refactoring_goal: str
    temperature: Optional[float] = 0.3

class ReviewResponse(BaseModel):
    review: str

class RefactoringResponse(BaseModel):
    response: str  # For now, raw response - could be structured JSON in future

@router.post("/code-review", response_model=ReviewResponse)
async def review_code(request: CodeReviewRequest):
    """Generate a code review for the provided code"""
    try:
        service = CodeReviewService()
        review = await service.review_code(
            code=request.code,
            language=request.language,
            quality_focus=request.quality_focus,
            perf_focus=request.perf_focus,
            security_focus=request.security_focus,
            style_focus=request.style_focus,
            additional_considerations=request.additional_considerations,
            temperature=request.temperature
        )
        return ReviewResponse(review=review)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code review failed: {str(e)}")

@router.post("/refactor", response_model=RefactoringResponse)
async def suggest_refactoring(request: RefactoringRequest):
    """Suggest code refactoring based on a specific goal"""
    try:
        service = CodeReviewService()
        result = await service.suggest_refactoring(
            code=request.code,
            language=request.language,
            refactoring_goal=request.refactoring_goal,
            temperature=request.temperature
        )
        return RefactoringResponse(response=result["response"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Refactoring suggestion failed: {str(e)}")
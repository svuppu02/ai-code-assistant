from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.services.code_explanation_service import CodeExplanationService

router = APIRouter()

class CodeExplanationRequest(BaseModel):
    code: str
    language: str
    detail_level: Optional[str] = "detailed"  # "brief", "detailed", or "comprehensive"
    additional_instructions: Optional[str] = ""
    temperature: Optional[float] = 0.3

class CodeIssuesRequest(BaseModel):
    code: str
    language: str
    temperature: Optional[float] = 0.2

class ExplanationResponse(BaseModel):
    explanation: str

@router.post("/code-explanation", response_model=ExplanationResponse)
async def explain_code(request: CodeExplanationRequest):
    """Generate an explanation for the provided code"""
    try:
        service = CodeExplanationService()
        explanation = await service.explain_code(
            code=request.code,
            language=request.language,
            detail_level=request.detail_level,
            additional_instructions=request.additional_instructions,
            temperature=request.temperature
        )
        return ExplanationResponse(explanation=explanation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code explanation failed: {str(e)}")

@router.post("/issues", response_model=ExplanationResponse)
async def identify_issues(request: CodeIssuesRequest):
    """Identify potential issues in the provided code"""
    try:
        service = CodeExplanationService()
        issues = await service.identify_code_issues(
            code=request.code,
            language=request.language,
            temperature=request.temperature
        )
        return ExplanationResponse(explanation=issues)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Issue identification failed: {str(e)}")
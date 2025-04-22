from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.services.code_generation_service import CodeGenerationService

router = APIRouter()

class CodeGenerationRequest(BaseModel):
    requirements: str
    language: str
    context: Optional[str] = ""
    temperature: Optional[float] = 0.2

class CodeCompletionRequest(BaseModel):
    code_snippet: str
    language: str
    instructions: str
    temperature: Optional[float] = 0.2

class CodeResponse(BaseModel):
    code: str

#@router.post("/code", response_model=CodeResponse)
import traceback

@router.post("/code-generation", response_model=CodeResponse)
async def generate_code(request: CodeGenerationRequest):
    try:
        service = CodeGenerationService()
        code = await service.generate_code(
            requirements=request.requirements,
            language=request.language,
            context=request.context,
            temperature=request.temperature
        )
        return CodeResponse(code=code)
    except Exception as e:
        # Log the full exception traceback for debugging
        print(f"Error in generate_code: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Code generation failed: {str(e)}")

@router.post("/complete", response_model=CodeResponse)
async def complete_code(request: CodeCompletionRequest):
    """Complete or modify existing code"""
    try:
        service = CodeGenerationService()
        code = await service.complete_code(
            code_snippet=request.code_snippet,
            language=request.language,
            instructions=request.instructions,
            temperature=request.temperature
        )
        return CodeResponse(code=code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code completion failed: {str(e)}")
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.services.documentation_service import DocumentationService

router = APIRouter()

class DocGenerationRequest(BaseModel):
    code: str
    language: str
    doc_type: Optional[str] = "API"  # API, function, class, module, etc.
    style: Optional[str] = "standard"  # standard, detailed, minimal
    format: Optional[str] = "markdown"  # markdown, JSDoc, docstring, etc.
    context: Optional[str] = ""
    temperature: Optional[float] = 0.3

class ReadmeGenerationRequest(BaseModel):
    project_name: str
    project_description: str
    features: List[str]
    installation_steps: List[str]
    usage_examples: Optional[List[str]] = None
    temperature: Optional[float] = 0.3

class DocumentationResponse(BaseModel):
    documentation: str

@router.post("/generate", response_model=DocumentationResponse)
async def generate_documentation(request: DocGenerationRequest):
    """Generate documentation for the provided code"""
    try:
        service = DocumentationService()
        documentation = await service.generate_documentation(
            code=request.code,
            language=request.language,
            doc_type=request.doc_type,
            style=request.style,
            format=request.format,
            context=request.context,
            temperature=request.temperature
        )
        return DocumentationResponse(documentation=documentation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Documentation generation failed: {str(e)}")

@router.post("/readme", response_model=DocumentationResponse)
async def generate_readme(request: ReadmeGenerationRequest):
    """Generate a README.md file for a project"""
    try:
        service = DocumentationService()
        readme = await service.generate_readme(
            project_name=request.project_name,
            project_description=request.project_description,
            features=request.features,
            installation_steps=request.installation_steps,
            usage_examples=request.usage_examples,
            temperature=request.temperature
        )
        return DocumentationResponse(documentation=readme)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"README generation failed: {str(e)}")
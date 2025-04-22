from typing import Dict, List, Optional, Any
import os
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager

from app.core.config import settings


class LLMService:
    """Base service for LLM operations"""

    def __init__(self):
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        """Initialize the LLM based on configuration"""
        if settings.LLM_PROVIDER == "openai":
            return ChatOpenAI(
                model_name=settings.DEFAULT_MODEL,
                temperature=0.2,
                openai_api_key=settings.OPENAI_API_KEY
            )
        else:
            # Add support for other LLM providers as needed
            raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")

    async def generate_response(self, prompt: str, temperature: float = 0.2) -> str:
        """Generate a response using the LLM"""
        if settings.LLM_PROVIDER == "openai":
            self.llm.temperature = temperature
            response = await self.llm.apredict(prompt)
            return response
        else:
            raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")
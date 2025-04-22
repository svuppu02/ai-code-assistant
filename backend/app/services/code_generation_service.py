from typing import Dict, Optional
from app.services.llm_service import LLMService


class CodeGenerationService(LLMService):
    """Service for generating code using LLMs"""

    CODE_GENERATION_PROMPT = """
    You are an expert programmer who writes clean, efficient, and well-documented code.

    Task: Generate code based on the following requirements:
    ```
    {requirements}
    ```

    Programming language: {language}
    Additional context: {context}

    Respond only with the code implementation, without explanations or markdown formatting.
    """

    async def generate_code(
            self,
            requirements: str,
            language: str,
            context: Optional[str] = "",
            temperature: float = 0.2
    ) -> str:
        """Generate code based on requirements"""
        prompt = self.CODE_GENERATION_PROMPT.format(
            requirements=requirements,
            language=language,
            context=context
        )

        return await self.generate_response(prompt, temperature)

    async def complete_code(
            self,
            code_snippet: str,
            language: str,
            instructions: str,
            temperature: float = 0.2
    ) -> str:
        """Complete or modify existing code based on instructions"""
        prompt = f"""
        You are an expert programmer. Complete or modify the following {language} code according to these instructions:

        Instructions: {instructions}

        Existing code:
        ```{language}
        {code_snippet}
        ```

        Respond only with the complete code after your modifications, without explanations or markdown formatting.
        """

        return await self.generate_response(prompt, temperature)
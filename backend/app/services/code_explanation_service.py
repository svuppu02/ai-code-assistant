from typing import Dict, Optional
from app.services.llm_service import LLMService


class CodeExplanationService(LLMService):
    """Service for explaining code using LLMs"""

    CODE_EXPLANATION_PROMPT = """
    You are an expert programmer who excels at explaining code in a clear and concise manner.

    Task: Explain the following code:
    ```{language}
    {code}
    ```

    Provide a {detail_level} explanation that covers:
    - What the code does overall
    - How it works step by step
    - Any important patterns or concepts used

    {additional_instructions}
    """

    async def explain_code(
            self,
            code: str,
            language: str,
            detail_level: str = "detailed",
            additional_instructions: str = "",
            temperature: float = 0.3
    ) -> str:
        """Generate an explanation for the provided code"""
        prompt = self.CODE_EXPLANATION_PROMPT.format(
            code=code,
            language=language,
            detail_level=detail_level,
            additional_instructions=additional_instructions
        )

        return await self.generate_response(prompt, temperature)

    async def identify_code_issues(
            self,
            code: str,
            language: str,
            temperature: float = 0.2
    ) -> str:
        """Identify potential issues or bugs in the code"""
        prompt = f"""
        You are an expert code reviewer with deep knowledge of {language} programming.

        Task: Analyze the following code for potential issues, bugs, or improvements:
        ```{language}
        {code}
        ```

        Identify and explain:
        1. Potential bugs or runtime errors
        2. Performance issues
        3. Security vulnerabilities
        4. Readability concerns
        5. Best practice violations

        For each issue, provide a clear explanation of the problem and a recommended solution.
        """

        return await self.generate_response(prompt, temperature)
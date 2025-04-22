from typing import Dict, List, Optional, Any
from app.services.llm_service import LLMService


class CodeReviewService(LLMService):
    """Service for reviewing code using LLMs"""

    CODE_REVIEW_PROMPT = """
    You are an expert code reviewer with deep knowledge of programming best practices.

    Task: Review the following {language} code:
    ```{language}
    {code}
    ```

    Focus on the following aspects:
    - Code quality: {quality_focus}
    - Performance: {perf_focus}
    - Security: {security_focus}
    - Style: {style_focus}

    Additional considerations: {additional_considerations}

    Provide a comprehensive code review with specific feedback and actionable suggestions for improvement.
    """

    async def review_code(
            self,
            code: str,
            language: str,
            quality_focus: bool = True,
            perf_focus: bool = True,
            security_focus: bool = True,
            style_focus: bool = True,
            additional_considerations: str = "",
            temperature: float = 0.3
    ) -> str:
        """Generate a code review for the provided code"""
        prompt = self.CODE_REVIEW_PROMPT.format(
            code=code,
            language=language,
            quality_focus="analyze code for readability, maintainability, and correct use of language features" if quality_focus else "skip",
            perf_focus="identify performance bottlenecks and suggest optimizations" if perf_focus else "skip",
            security_focus="identify potential security vulnerabilities" if security_focus else "skip",
            style_focus="check adherence to coding standards and style guides" if style_focus else "skip",
            additional_considerations=additional_considerations
        )

        return await self.generate_response(prompt, temperature)

    async def suggest_refactoring(
            self,
            code: str,
            language: str,
            refactoring_goal: str,
            temperature: float = 0.3
    ) -> Dict[str, Any]:
        """Suggest code refactoring based on a specific goal"""
        prompt = f"""
        You are an expert in code refactoring with deep knowledge of {language} programming.

        Task: Suggest refactoring for the following code to achieve this goal: {refactoring_goal}

        Original code:
        ```{language}
        {code}
        ```

        Provide a JSON response with the following structure:
        {{
            "analysis": "Explanation of what needs to be refactored and why",
            "refactored_code": "The complete refactored code",
            "changes_summary": "Summary of the changes made during refactoring"
        }}

        Focus on meaningful improvements that achieve the stated goal while maintaining the original functionality.
        """

        response = await self.generate_response(prompt, temperature)

        # In a real implementation, we'd parse the JSON response here
        # For now, returning the raw response
        return {"response": response}
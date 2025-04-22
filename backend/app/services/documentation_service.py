from typing import Dict, List, Optional
from app.services.llm_service import LLMService


class DocumentationService(LLMService):
    """Service for generating documentation using LLMs"""

    DOC_GENERATION_PROMPT = """
    You are an expert technical writer who creates clear, comprehensive documentation.

    Task: Generate {doc_type} documentation for the following {language} code:
    ```{language}
    {code}
    ```

    Documentation style: {style}
    Format requirements: {format}
    Additional context: {context}

    Create thorough, accurate documentation that would help developers understand and use this code effectively.
    """

    async def generate_documentation(
            self,
            code: str,
            language: str,
            doc_type: str = "API",  # API, function, class, module, etc.
            style: str = "standard",  # standard, detailed, minimal
            format: str = "markdown",  # markdown, JSDoc, docstring, etc.
            context: str = "",
            temperature: float = 0.3
    ) -> str:
        """Generate documentation for the provided code"""
        prompt = self.DOC_GENERATION_PROMPT.format(
            code=code,
            language=language,
            doc_type=doc_type,
            style=style,
            format=format,
            context=context
        )

        return await self.generate_response(prompt, temperature)

    async def generate_readme(
            self,
            project_name: str,
            project_description: str,
            features: List[str],
            installation_steps: List[str],
            usage_examples: List[str] = None,
            temperature: float = 0.3
    ) -> str:
        """Generate a README.md file for a project"""
        features_str = "\n".join([f"- {feature}" for feature in features])
        installation_str = "\n".join([f"{i + 1}. {step}" for i, step in enumerate(installation_steps)])

        usage_str = ""
        if usage_examples:
            usage_str = "\n".join([f"```\n{example}\n```" for example in usage_examples])

        prompt = f"""
        Create a professional README.md file for a project with the following details:

        Project Name: {project_name}
        Project Description: {project_description}

        Features:
        {features_str}

        Installation:
        {installation_str}

        Usage Examples:
        {usage_str}

        Include the following sections:
        - Title and Description
        - Features
        - Installation
        - Usage
        - Contributing (with standard open-source guidelines)
        - License (MIT)

        Format the README using proper Markdown syntax with headers, code blocks, and formatting.
        """

        return await self.generate_response(prompt, temperature)
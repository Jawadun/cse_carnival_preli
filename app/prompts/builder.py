from typing import Dict

from app.prompts.templates import PROMPT_TEMPLATES


class PromptBuilder:
    def build(self, template_name: str, context: Dict[str, str]) -> str:
        # TODO: render prompt template with supplied context
        return PROMPT_TEMPLATES.get(template_name, "")

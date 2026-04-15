from schemas.class_ import ClassReportRequest, ClassReportResponse
from prompts.class_prompt import build_class_prompt
from llm.openai_client import OpenAIClient
import json

async def generate_class_report(request: ClassReportRequest) -> ClassReportResponse:
    prompt = build_class_prompt(request)
    llm_response = OpenAIClient.generate(prompt)
    # Try to extract valid JSON
    try:
        data = json.loads(llm_response)
    except Exception:
        # Attempt to extract JSON substring
        import re
        match = re.search(r'{[\s\S]*}', llm_response)
        if match:
            data = json.loads(match.group(0))
        else:
            raise ValueError("LLM did not return valid JSON.")
    return ClassReportResponse(**data)

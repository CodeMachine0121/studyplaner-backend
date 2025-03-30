from openai import OpenAI
from prompt_service import PromptService
from models.study_models import DailyPlan, StudyPlan, StudySubject

class AIService:
    """Service for interacting with AI models"""
    
    def __init__(self, openai_api_key=None, base_url=None, model=None):
        """Initialize the AI service with API keys"""
        self.openai_api_key = openai_api_key
        self.base_url = base_url
        self.model = model
        self.client = OpenAI(api_key=self.openai_api_key, base_url= self.base_url)
        self.promptService = PromptService()
    
    def process_study_content(self, study_subject: StudySubject, max_tokens=1000) -> StudyPlan:
        """
        Process study content using OpenAI's GPT model
        
        Args:
            content (str): The study content to process
            max_tokens (int): Maximum number of tokens in the response
            
        Returns:
            str: The processed content
        """
        if not study_subject.Subject:
            raise ValueError("Subject cannot be empty")
        
        # Chat template for processing study content
        messages = self.promptService.get_study_plan_prompt(study_subject)

        # Send request to OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=max_tokens
        )

        message = response.choices[0].message.content
        study_plan = StudyPlan.parse_raw(message)

        return study_plan
        
        
from typing import List, Dict, Any
import json

class PromptService:
    """
    Service for generating prompts for AI models
    """
    
    def get_study_plan_prompt(self, subject: str) -> List[Dict[str, str]]:
        """
        Generate a prompt for creating a 30-day study plan for a given subject
        
        Args:
            subject (str): The subject to create a study plan for
            
        Returns:
            List[Dict[str, str]]: List of message objects for the OpenAI API
        """
        # Example of the expected JSON structure
        example_json = {
            "DailyPlans": [
                {
                    "Day": 1,
                    "Title": "基礎概念入門",
                    "Content": "學習主題的基本概念和術語。重點掌握基礎理論，完成入門練習。"
                }, 
                {
                    "Day": 2,
                    "Title": "核心原理探索",
                    "Content": "深入了解核心原理，並完成相關練習和案例分析。"
                }
                # ... and so on for 30 days
            ]
        }
        
        # Convert the example to a string for the prompt
        example_json_str = json.dumps(example_json, ensure_ascii=False, indent=2)
        
        # Create the messages for the prompt
        messages = [
            {"role": "system", "content": "一律使用正體中文回答"},
            
            {"role": "system", "content": "你是一個專業的學習規劃助手，能夠為學生安排有效的學習計劃。"}, 
            
            {"role": "system", "content": f"你必須嚴格按照以下JSON格式輸出30天的學習計劃，每天必須包含Day(天數)、Title(當天學習的簡短標題)和Content(詳細的學習內容)三個欄位。請不要添加任何其他文字或解釋：\n{example_json_str}"}, 

            {"role": "user", "content": f"請為我安排一個30天的'{subject}'學習計劃。每天的計劃必須包含Day(天數)、Title(當天學習的簡短標題)和Content(詳細的學習內容)，文字長度大約1000字數即可(不含題目及實作）。請確保學習計劃循序漸進，由基礎到進階，並包含複習和練習的時間。"},

            {"role": "user", "content": f"Content 為當天學習的詳細內容，請提供詳細的學習說明，並提供相關的練習題目，包括答案"}
        ]
        
        return messages

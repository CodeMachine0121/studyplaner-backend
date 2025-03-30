from pydantic import BaseModel
from typing import List

class DailyPlan(BaseModel):
    """
    Model for a daily study plan
    """
    Day: int
    Title: str
    Content: str

class StudyPlan(BaseModel):
    """
    Model for a complete study plan consisting of multiple daily plans
    """
    DailyPlans: List[DailyPlan]

class StudySubject(BaseModel):
    """
    Model for a study subject request
    """
    Subject: str
    Description: str

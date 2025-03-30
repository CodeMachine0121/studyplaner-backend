from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from ai_service import AIService

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Study Planner Backend")

# Initialize AI service with environment variables
ai_service = AIService(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL_NAME", "grok-2-latest")
)

class StudySubject(BaseModel):
    Content: str

@app.post("/process-study")
async def process_study(subject: StudySubject):
    if not subject.Content:
        raise HTTPException(status_code=400, detail="Content cannot be empty")
    
    try:
        # Process study content using AI service with named parameters
        processed_content = ai_service.process_study_content(
            content=subject.Content,
            max_tokens=1000
        )
        return {"processed_content": processed_content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

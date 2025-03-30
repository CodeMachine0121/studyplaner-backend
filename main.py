from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
from ai_service import AIService
from models.study_models import StudySubject

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

# StudySubject model is now imported from models.study_models

@app.post("/process-study")
async def process_study(study_subject: StudySubject):
    if not study_subject.Subject:
        raise HTTPException(status_code=400, detail="Subject cannot be empty")
    
    try:
        # Process study content using AI service with named parameters
        processed_content = ai_service.process_study_content(
            study_subject=study_subject,
            max_tokens=15000
        )
        return {"processed_content": processed_content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

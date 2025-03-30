# Study Planner Backend

A FastAPI backend service that generates personalized 30-day study plans using AI models. The service takes a subject and description as input and returns a structured daily learning plan.

## Features

- Generate comprehensive 30-day study plans for any subject
- Each day includes a day number, title, and detailed content
- Content includes learning materials, exercises, and answers
- Structured JSON output for easy integration with frontend applications

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
- Copy `.env.example` to `.env`
- Add your API key, base URL, and model name to the `.env` file:
  ```
  OPENAI_API_KEY='your-api-key-here'
  BASE_URL='your-base-url-here'  # e.g., https://api.x.ai/v1
  MODEL_NAME='your-model-name-here'  # e.g., grok-2-latest
  ```

3. Run the server:
```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### POST /process-study

Generates a 30-day study plan for the given subject.

#### Request Body

```json
{
  "Subject": "Python Programming",
  "Description": "For beginners with no prior programming experience"
}
```

#### Response

```json
{
  "processed_content": {
    "DailyPlans": [
      {
        "Day": 1,
        "Title": "Python 基礎介紹",
        "Content": "詳細的學習內容..."
      },
      {
        "Day": 2,
        "Title": "變數與資料類型",
        "Content": "詳細的學習內容..."
      },
      // ... more days
    ]
  }
}
```

## Project Structure

- `main.py` - FastAPI application and endpoints
- `ai_service.py` - Service for interacting with AI models
- `prompt_service.py` - Service for generating prompts for AI models
- `.env` - Environment variables (not tracked in git)
- `.env.example` - Example environment variables

# Study Planner Backend

A FastAPI backend service that processes study content using OpenAI's GPT model.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
- Copy `.env.example` to `.env`
- Add your OpenAI API key to the `.env` file

3. Run the server:
```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### POST /process-study

Process study content through OpenAI's GPT model.

Request body:
```json
{
    "Content": "Your study content here"
}
```

Response:
```json
{
    "processed_content": "GPT-processed study content"
}
```

### POST /process-study-grok

Process study content through Grok AI (currently a mock implementation).

Request body:
```json
{
    "Content": "Your study content here"
}
```

Response:
```json
{
    "processed_content": "Grok AI-processed study content"
}
```

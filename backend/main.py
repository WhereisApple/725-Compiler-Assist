from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from compiler import run_python, run_c
from assistant import generate_response
from analyzer import explain_error


app = FastAPI(title="725 Compiler Assist API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "725 Compiler Assist Backend is Running 🚀"
    }


@app.post("/run")
async def run(data: dict):

    language = data.get("language", "")
    code = data.get("code", "")

    if language == "python":
        result = run_python(code)

    elif language == "c":
        result = run_c(code)

    else:
        return {
            "stdout": "",
            "stderr": "Language not supported yet.",
            "language": language
        }

    return {
        "stdout": result.get("stdout", ""),
        "stderr": result.get("stderr", ""),
        "language": language
    }


@app.post("/assistant")
async def assistant(data: dict):

    code = data.get("code", "")
    language = data.get("language", "")
    question = data.get("question", "")

    answer = generate_response(
        code,
        language,
        question
    )

    return {
        "answer": answer
    }


@app.post("/explain_error")
async def explain(data: dict):

    error = data.get("error", "")
    language = data.get("language", "")

    explanation = explain_error(
        error,
        language
    )

    return {
        "explanation": explanation
    }

@app.post("/analyze")
async def analyze(data: dict):

    code = data.get("code", "")
    language = data.get("language", "")

    question = "Suggest improvements for my code"

    answer = generate_response(
        code,
        language,
        question
    )

    return {
        "analysis": answer
    }

from analyzer import explain_error


@app.post("/explain_error")
async def explain(data: dict):

    error = data.get("error", "")

    language = data.get("language", "python")


    result = explain_error(
        error,
        language
    )


    return {
        "answer": result
    }
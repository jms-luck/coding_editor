from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from executor.executor import run_python_code, run_java_code, run_c_code, run_cpp_code


app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Code(BaseModel):
    language: str
    code: str

@app.post("/run")
def run_code(payload: Code):
    try:
        if payload.language == "python":
            output = run_python_code(payload.code)
            return {"output": output}
        elif payload.language == "java":
            output = run_java_code(payload.code)
            return {"output": output}
        elif payload.language == "c":
            output = run_c_code(payload.code)
            return {"output": output}
        elif payload.language == "cpp":
            output = run_cpp_code(payload.code)
            return {"output": output}
        else:
            return {"output": "Unsupported language"}
    except Exception as e:
        return {"output": f"Error: {str(e)}"}

@app.get("/health")
def health():
    return {"status": "ok"}
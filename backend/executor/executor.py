import subprocess
import tempfile
import os

def run_python_code(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        filename = f.name

    try:
        result = subprocess.run(
            ["docker", "run", "--rm",
             "-v", f"{filename}:/app/code.py",
             "python-runner"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout + result.stderr
    finally:
        os.remove(filename)

def run_java_code(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".java") as f:
        f.write(code.encode())
        filename = f.name

    try:
        result = subprocess.run(
            ["docker", "run", "--rm",
             "-v", f"{filename}:/app/code.java",
             "java-runner"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout + result.stderr
    finally:
        os.remove(filename)

def run_c_code(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f:
        f.write(code.encode())
        filename = f.name

    try:
        result = subprocess.run(
            ["docker", "run", "--rm",
             "-v", f"{filename}:/app/code.c",
             "c-runner"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout + result.stderr
    finally:
        os.remove(filename)

def run_cpp_code(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp") as f:
        f.write(code.encode())
        filename = f.name

    try:
        result = subprocess.run(
            ["docker", "run", "--rm",
             "-v", f"{filename}:/app/code.cpp",
             "cpp-runner"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout + result.stderr
    finally:
        os.remove(filename)
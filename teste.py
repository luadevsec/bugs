
import subprocess
def start_server():
    command = [
        "uvicorn",
        "test:prototipo",
        "--host", "localhost",
        "--port", "7777",
        "--reload"
    ]
    
    subprocess.run(command)
if __name__ == "__main__":
    start_server()


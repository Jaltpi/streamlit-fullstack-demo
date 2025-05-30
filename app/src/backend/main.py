from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hi")
def greet():
    return 'hi'

def hello_world():
    return 'hello world'

def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()

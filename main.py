from users.models import User, Gender
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
  return "Hello world"



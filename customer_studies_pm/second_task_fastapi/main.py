from fastapi import FastAPI
from get_weaknesses import task

# Initialize the app
app = FastAPI()

# GET operation at route '/'
@app.get('/')
async def index():
    return {"greeting" : "Welcome to Microsoft!"}

@app.get('/pokemon_weakness')
async def pokemon():
    return task()
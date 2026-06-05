from fastapi import FastAPI
from telegrambot.bot import start

app = FastAPI()

@app.on_event('shutdown')
def shutdown_event():
    start()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('fastapi.app', host='0.0.0.0', port=8000)
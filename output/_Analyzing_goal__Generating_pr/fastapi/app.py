from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI()

@app.get('/')
def read_root():
    return JSONResponse(content={'message': 'Hello World'}, media_type='application/json')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)
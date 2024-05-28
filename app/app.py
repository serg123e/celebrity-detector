import os
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from celeb_detector import celeb_recognition

print("Loaded: celeb_detector")

API_TOKEN = os.getenv("API_TOKEN")
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

if API_TOKEN:
  print("API_TOKEN specified, authorization enabled") 
else:
  print("API_TOKEN not specified, authorization DISABLED. Do not expose the service to public") 

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_api_key(api_key_header: str = Depends(api_key_header)):
    if API_TOKEN and api_key_header != API_TOKEN:

        raise HTTPException(status_code=403, detail=f"Could not validate credentials {api_key_header} <=> {API_TOKEN}")
    return api_key_header

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), api_key: str = Depends(get_api_key)):
    if not file:
        raise HTTPException(status_code=400, detail="No file part")

    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")

    temp_path = os.path.join('/tmp', file.filename)
    with open(temp_path, "wb") as buffer:
        buffer.write(file.file.read())

    response = {}

    try:
        celeb_detector_results = celeb_recognition.get_celebrity(temp_path)
        response['celeb_detector'] = celeb_detector_results
    finally:
        # Optionally remove the file if you no longer need it
        os.remove(temp_path)

    return JSONResponse(content=response)

@app.get("/", response_class=HTMLResponse)
async def get_form():
    html_content = """
    <html>
        <head>
            <title>Upload File</title>
        </head>
        <body>
            <h1>Upload File for Celebrity Recognition</h1>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)

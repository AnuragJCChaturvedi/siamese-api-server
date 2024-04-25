import uvicorn
from fastapi import FastAPI, File, UploadFile
from routes.predict import findSimilarity as fs
from routes.liveliness import checkliveness
from starlette.middleware.cors import CORSMiddleware
 
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
 
@app.get("/")
def read_root():
    return "API Server is Up!"

@app.post("/predict")
async def findSimilarity(webcam_image: UploadFile = File(...)):
    webcam_image_data = await webcam_image.read()
    return await fs(webcam_image_data)

@app.get("/dryrun")
async def findSimilarity():
    return await fs(None)

@app.post("/check-liveliness")
async def checkLiveliness(webcam_image: UploadFile = File(...)):
    webcam_image_data = await webcam_image.read()
    return await checkliveness(webcam_image_data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3001)
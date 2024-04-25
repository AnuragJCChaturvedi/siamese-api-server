import httpx
import os
from fastapi import HTTPException
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

LivelinessThreshold = 0.99

async def checkliveness(webcam_image):
    async with httpx.AsyncClient() as client:
        files = {
            "image": ("webcam_image.jpg", BytesIO(webcam_image), 'image/jpeg')
        }
        url = f"{os.getenv('model_server')}/check-liveness"
        response = await client.post(url, files=files)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error processing the image.")
        
        data = response.json()
        accuracy = data.get('accuracy')

        print("Liveliness accuracy: ", accuracy)
        
        return {"liveliness": accuracy >= LivelinessThreshold}


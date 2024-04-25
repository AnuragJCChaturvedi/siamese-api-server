from fastapi import HTTPException
from db_conn import connect_to_database
from io import BytesIO
from dotenv import load_dotenv

import httpx
import os
import asyncio

load_dotenv()

SimilarityThreshold = 0.01

async def get_user_details(user_id):
    conn = await connect_to_database()
    try:
        row = await conn.fetchrow("SELECT id, firstName, lastName, amount FROM users WHERE id = $1", user_id)
        return dict(row)
    finally:
        await conn.close()
        
async def get_all_images():
    """Retrieve all images from the database asynchronously."""
    conn = await connect_to_database()
    try:
        rows = await conn.fetch('SELECT "rawimage", "userid" FROM images')
        # Extract rawImage from each row
        images = [{'rawImage': row['rawimage'], 'userId': row['userid']} for row in rows]
        return images
    except Exception as e:
        print(f"Failed to fetch images: {e}")  # Better error diagnostics
        return []
    finally:
        await conn.close()

async def findSimilarity(webcam_image):
    all_images = await get_all_images()
    async with httpx.AsyncClient() as client:
        tasks = []
        results = []
        
        for row in all_images:
            db_image_data, user_id = row['rawImage'], row['userId']
            files = {
                "image1": ("webcam_image.jpg", BytesIO(webcam_image), 'image/jpeg'),
                "image2": ("db_image.jpg", BytesIO(db_image_data), 'image/jpeg')
            }
            url = f"{os.getenv('model_server')}/siamese/predict"
            task = (client.post(url, files=files), user_id) 
            tasks.append(task)
        
        responses = await asyncio.gather(*[t[0] for t in tasks], return_exceptions=True)
        
        for response, (task, user_id) in zip(responses, tasks):
            if isinstance(response, httpx.Response) and response.status_code == 200:
                prediction_result = response.json()
                print(prediction_result)
                accuracy = prediction_result.get('accuracy', 0)
                if accuracy >= SimilarityThreshold:
                    user_details = await get_user_details(user_id)
                    results.append({
                        "accuracy": accuracy,
                        "user": {
                            "faceId": user_details['id'],
                            "firstName": user_details['firstname'],
                            "lastName": user_details['lastname'],
                            "amount": user_details['amount']
                        }
                    })
            elif isinstance(response, Exception):
                print(f"Request failed: {response}")
        
        # Sort results by accuracy in descending order
        results.sort(key=lambda x: x['accuracy'], reverse=True)
        
        return results


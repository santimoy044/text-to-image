from fastapi import APIRouter, Request, HTTPException
from app.services.image_generator import generate_image

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Text-to-Image API is running!"}

@router.post("/generate")
async def generate(request: Request):
    try:
        body = await request.json()
        prompt = body.get("prompt")
        
        if not prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
            
        image_path = generate_image(prompt)
        return {"image_path": image_path}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

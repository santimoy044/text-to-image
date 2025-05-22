from diffusers import StableDiffusionPipeline
import torch
from config import MODEL_NAME, DEVICE

pipe = None

def get_pipeline():
    global pipe
    if pipe is None:
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32
        )
        pipe = pipe.to(DEVICE)
    return pipe

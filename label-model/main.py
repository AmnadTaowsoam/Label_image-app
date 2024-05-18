from fastapi import FastAPI
from pydantic import BaseModel
from config import settings
from pre_processing import load_model as load_pre_model, predict as predict_pre
from re_processing import load_model as load_re_model, predict as predict_re
from db import store_pre_label_in_db, store_re_label_in_db

app = FastAPI()

pre_model = load_pre_model(settings.pre_label_model_name, settings.pre_label_model_path)
re_model = load_re_model(settings.re_label_model_name, settings.re_label_model_path)

class ImageRequest(BaseModel):
    image: str

@app.post('/pre_predict')
async def pre_predict_route(request: ImageRequest):
    img = request.image
    predictions = predict_pre(pre_model, img)
    return {"predictions": predictions}

@app.post('/re_predict')
async def re_predict_route(request: ImageRequest):
    img = request.image
    predictions = predict_re(re_model, img)
    return {"predictions": predictions}

@app.post('/store_pre_label')
async def store_pre_label_route(image_path: str, label: dict):
    pre_label_id = store_pre_label_in_db(image_path, label)
    return {"pre_label_id": pre_label_id}

@app.post('/store_re_label')
async def store_re_label_route(pre_label_id: int, image_path: str, label: dict):
    store_re_label_in_db(pre_label_id, image_path, label)
    return {"status": "success"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=settings.api_host, port=settings.pre_label_api_port)

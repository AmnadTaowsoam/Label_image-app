import torch

def load_model(model_name, model_path):
    model = torch.hub.load('ultralytics/yolov5', model_name)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def predict(model, image):
    results = model(image)
    return results.xyxy[0].tolist()

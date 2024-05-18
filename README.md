# Label_image-app

## label-model

1. create Environment

   python -m venv venv
   .\venv\Scripts\activate

## docker-compose

1. run docker-compose

   docker-compose up -d

2. down docker-compose

   docker-compose down

3. Re build docker-compose

   docker-compose up --build -d

.env

# Pre-label model configuration

PRE_LABEL_MODEL_NAME=yolov5
PRE_LABEL_MODEL_PATH=path/to/pretrained/model

# Re-label model configuration

RE_LABEL_MODEL_NAME=yolov5
RE_LABEL_MODEL_PATH=path/to/retrained/model

# API configuration

API_HOST=0.0.0.0
PRE_LABEL_API_PORT=5000
RE_LABEL_API_PORT=5001

# Database configuration

DB_NAME=labelstudio
DB_USERNAME=postgres
DB_PASSWORD=password
DB_HOST=image-storage
DB_PORT=5432

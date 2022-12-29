# Image Detection project - HanBok  

## How to run
### Install Requirements
Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.7 (per https://github.com/ultralytics/yolov5).

```pip install -r requirements.txt```

### Run to Train:
```python train.py --data {dataset.location}/data.yaml --weights yolov5s.pt ```

### Get Result:
```python detect.py```

---
## How to run API

### Summary
This is a FastAPI app that allows a user to upload image(s), perform inference using a pretrained  model, and receive results in JSON format. This repo also includes Jinja2 HTML templates, so you can access this interface through a web browser at `localhost:8000`.

### To run:   
1. Access `cv_detection/api` directory

2. Run this in terminal:  
```python server.py```

3. Access web browser at `localhost:8000`

Reference github : https://github.com/WelkinU/yolov5-fastapi-demo

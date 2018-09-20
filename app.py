

from flask import Flask, request, jsonify, json

from yolo import YOLO

from PIL import Image

from util import TestDataProvider

from util import JsonUtil
from util import ImageLoader
from util import OcrEngine
from util import ImageMarker

import numpy as np

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

_args = {
        "model_path": 'anet-tiny/anet.h5',
        "anchors_path": 'anet-tiny/anchors.txt',
        "classes_path": 'anet-tiny/classes.txt',
        "score" : 0.3,
        "iou" : 0.45,
        "model_image_size" : (1024, 768),
        "gpu_num" : 1,
    }

yoloInstance = None

@app.route('/detect', methods=('get', 'post'))
def detect():
    global yoloInstance
    if yoloInstance == None:
        yoloInstance = YOLO()
    
    jsonObj = request.get_json()
    if (jsonObj == None):
        return None, 500

    type = jsonObj.get('type')
    data = jsonObj.get('data')

    image = ImageLoader.get_image(type, data)
    if image == None:
        return "Cannot load image!", 400

    result = yoloInstance.detect_image(image)

    for item in result:
        box = item.get('box')
        arr = ['left', 'top', 'right', 'bottom']
        cropBox = tuple(map(lambda key: box[key], arr))
        cropImage = image.crop(cropBox)
        text = OcrEngine.process_image(cropImage)
        item['text'] = text

    ImageMarker.mark_image(image, result)

    return JsonUtil.stringify(result)

@app.route('/test', methods=('get', 'post'))
def test():
    arr = np.array([1,2,3])
    obj = {"hello": arr[0]}

    image = TestDataProvider.get_test_image()
    text = OcrEngine.process_image(image)

    return JsonUtil.stringify(obj)

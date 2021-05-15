import os
import time

import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, request, Response, abort, jsonify
import subprocess

# Initialize Flask application
app = Flask(__name__)


# API that returns image with detections on it
@app.route('/image', methods=['POST'])
def get_image():
    image = request.files["images"]
    image_name = image.filename
    image.save(os.path.join(os.getcwd(), image_name))
    command = "python detect.py --images {} ".format(
        image_name)
    # subprocess.run(command)
    os.system(command)

    # remove temporary image
    # os.remove(image_name)
    # image_result = os.path.join(os.getcwd(), 'detection1.png')
    # _, img_encoded = cv2.imencode('.png', image)
    response = "Done"

    try:
        return jsonify({"response":response}), 200
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

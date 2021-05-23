import os

import core.detection_tf as dtf
import cv2
import numpy as np
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import tensorflow as tf
from flask import Flask, request, Response, jsonify, send_from_directory, abort
import json

# Initialize Flask application
app = Flask(__name__)


# API that returns image with detections on it
@app.route('/image', methods=['POST'])
def get_image():
    category_index = label_map_util.create_category_index_from_labelmap('./Tensorflow/annotations/label_map.pbtxt')

    image = request.files["images"]
    IMAGE_REQUEST = image.filename
    image.save(os.path.join(os.getcwd(), 'detections', 'tmp', IMAGE_REQUEST))
    IMAGE_PATH = os.path.join(os.getcwd(), 'detections', 'tmp', IMAGE_REQUEST)
    command = "python detect.py --images ./detections/tmp/{} ".format(
        IMAGE_REQUEST)
    os.system(command)

    IMAGE_CROPPED = os.path.join(os.getcwd(), 'detections', 'crop', 'license_plate_1.png')

    img = cv2.imread(IMAGE_CROPPED)
    image_np = np.array(img)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = dtf.detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()
    boxes = detections['detection_boxes']
    max_boxes_to_draw = 8
    scores = detections['detection_scores']
    class_idx = detections['detection_classes'] + label_id_offset
    min_score_thresh = 0.5

    result = []
    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores[i] > min_score_thresh:
            item = {"label": category_index[class_idx[i]]["name"],
                    "score": scores[i],
                    "boxes": boxes[i][1]
                    }
            result.append(item)

    result = sorted(result, key=lambda k: k['boxes'])
    digit_plate = ""
    for digit in result:
        digit_plate = digit_plate + digit["label"]

    print("digits detected: ", digit_plate)

    try:
        return jsonify({"response": digit_plate}), 200
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

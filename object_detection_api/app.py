import os

# import core.detection_tf as dtf
# import cv2
# import numpy as np
# from object_detection.utils import label_map_util
# from object_detection.utils import visualization_utils as viz_utils
# import tensorflow as tf
from flask import Flask, request, Response, jsonify, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
import json

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/license_plate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret-key'

db = SQLAlchemy(app)

# Database model
class Plate(db.Model):
    __tablename__ = 'plate_numbers'

    id_user = db.Column(db.Integer)
    id_transaction = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(8), unique=True)
    place = db.Column(db.String(64))
    time_enter = db.Column(db.DateTime(timezone=True))
    time_out = db.Column(db.DateTime(timezone=True))
    price = db.Column(db.Numeric())

    def __init__(self, id_user, id_transaction, plate_number, place):
        self.id_user = id_user
        self.id_transaction = id_transaction
        self.plate_number = plate_number
        self.place = place

    def __repr__(self) -> str:
        return '<id_transaction {}>'.format(self.id_transaction)

    def serialize(self):
        return {
            'id_user': self.id_user,
            'id_transaction': self.id_transaction,
            'plate_number': self.plate_number,
            'place': self.place,
            'time_enter': self.time_enter,
            'time_out': self.time_out,
            'price': self.price
        }

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

    plate_exist = db.session.query(Plate.id_user).filter_by(plate_number=digit_plate).scalar() is not None

    if plate_exist:
        return jsonify({"plate_number": digit_plate, "is_exist": plate_exist is not None}), 200
    else:
        return jsonify({"response": f"User with {digit_plate} plate number not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

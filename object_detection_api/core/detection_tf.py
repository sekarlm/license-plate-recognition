import os
import tensorflow as tf

from object_detection.utils import label_map_util, config_util
from object_detection.builders import model_builder

configs = config_util.get_configs_from_pipeline_file('./Tensorflow/workspace/efficientdet_d1_coco17/pipeline.config')
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join('./Tensorflow/workspace/efficientdet_d1_coco17/', 'ckpt-6')).expect_partial()


@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

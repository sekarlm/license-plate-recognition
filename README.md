<br />
<p align="center">
  <h2 align="center">Next Parking Plate Number Reader</h2>
  <h3 align="center">Pay, save and track your parking.</h3>
</p>


## Built With

- [Tensorflow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)
- [Google Colab](https://colab.research.google.com/)

## Technique Used

### Object Plate Detection

<YOLO v4 technique>

### Digit Number Detection
We use TensorFlow Object Detection Api with EfficientDet D1 model for our digit number detector. TensorFlow Object Detection Api make it easy to localizing and identifying multiple objects (digit numbers) in a single image (plate number image). EfficientDet D1 model which previously trained on our dataset try to produce object class and bounding box predictions respectively of each digit numbers in a single plate number with highest similarity score.
You can see the detail of our training process and dataset that we use [here](#).

## State of Arts or Journal

### Object Plate Detection

<SOTA YOLO v4>

### Digit Number Recognition

<SOTA EfficientDet D1>

## Explanation For Workflow
![Images](https://github.com/sekarlm/license-plate-recognition/blob/main/contents/ML_flow_result.png)

## Acknowledgements


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
This is our training result:
<p align="center">
    <img src="contents/EfficientDet_training.png" alt="Training Result" height="350">
</p>
After we trained the model on 441 images of Indonesian License Plate Number, we got 89.7% mAP over 50% IOU threshold and 82.6% mAP over 75% IOU threshold.

You can see the detail of our training process and dataset that we use [here](#).

## State of Arts or Journal

### Object Plate Detection

<SOTA YOLO v4>

### Digit Number Recognition
<p align="center">
    <img src="contents/EfficientDet.png" alt="EfficientDet Graph" height="350">
</p>
<p>As you can see from the graph above, efficientDet achieves state-of-the-art accuracy while being up to <b>9x smaller</b> and using up to <b>43x fewer computation</b> compared to prior state-of-the-art detectors.</p>
<p align="center">
    <img src="contents/EfficientDetD1.png" alt="Table EfficientDet D1" width="550">
</p>
<p>For this project we choose EfficientDet D1. As you can see from the table, compared to the other models in the same distribution, it achieves higher accuracy with 39.6 Average Precision, uses much fewer parameters (6.6 M), and uses fewer computation operations (6.1B FLOPs).</p>

You can read the complete journal [here](#).

## Explanation For Workflow
<p align="center">
    <img src="contents/ML_flow_result.png" alt="EfficientDet Graph" height="600">
</p>

## Acknowledgements


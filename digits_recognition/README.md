# Training EfficientDet for Digits License Plate Recognition

In this notebook, I use TensorFlow Object Detection Api to train custom object detection using EfficientDet D1.

## Getting Started

We use 441 raw images of license plate number as dataset. Before training the model on our dataset, we preprocess all images to create label of it. We use labelImg to create bounding box of each digits number in image and then give each digits label. We split the dataset into 90% train data and 10% test data.

You can use my dataset here: [download][Google Drive]

You can find the instructions to install all the dependencies for training model in the notebook.

## Training

Please follow all the instruction in ipynb file. I try to explain in there clearly.

[Google Drive]: https://drive.google.com/file/d/1ocBdTxUxnLdgPd9JhpK1m2WRfctjeLYE/view?usp=sharing
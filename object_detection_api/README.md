# Getting started

Get file from here for [model](https://drive.google.com/file/d/1PDwGnslECSfl07tBk0Go0piXEihkGzQr/view?usp=sharing). Make ``checkpoints`` directory in this folder and unzip downloaded model to ``checkpoints`` directory.

Run 2 commands to make directory to save file:

``mkdir detections``

``mkdir detections/crop && mkdir detections/tmp``

And then run this command to install requirements.

``pip install -r requirements.txt``

Now we move to digit detections to read plate number.

First make ``Tensorflow`` directory and in there, there are ``Model, protoc, and workspace directory`` so make sure to mkdir it also.

download annotations [here.](https://drive.google.com/file/d/1P8vAD65FzA2OWH9bfk2wrf0wJkp4RQ4N/view?usp=sharing)

then clone tensorflow models from [here,](https:/github.com/tensorflow/models) to Tensorflow/models

And then install protobuf compiler using ``apt-get install protobuf-compiler``

Run these following commands :

``cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && sudo python -m pip install .``

After no error detected, run **``python app.py``** and flask server will start automatically.

## Credits

Thank you [theAIGuysCode](https://github.com/theAIGuysCode/yolov4-custom-functions). We edit the code and add another object detection to fit our purpose. 
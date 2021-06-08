# Getting started

Get file from here for [model](https://drive.google.com/file/d/1PDwGnslECSfl07tBk0Go0piXEihkGzQr/view?usp=sharing). 

1. Make **checkpoints** directory in this folder and unzip downloaded model to **checkpoints** directory.

2. Run 2 commands to make directory to save file:

```
mkdir detections && mkdir detections/crop && mkdir detections/tmp
```

3. run this command to install requirements.

```
pip install -r requirements.txt
```

## Run object detection API.

### *Note: You need linux to run this steps. 

1. First make Tensorflow directory and in there, there are 
   ```
   mkdir Tensorflow && mkdir Tensorflow/model && mkdir detections/protoc && Tensordflow/workspace
   ```

2. Download annotations [here.](https://drive.google.com/file/d/1P8vAD65FzA2OWH9bfk2wrf0wJkp4RQ4N/view?usp=sharing)

3. clone tensorflow models from [here,](https:/github.com/tensorflow/models) to Tensorflow/models

4. then install protobuf compiler using ``apt-get install protobuf-compiler``

5. Run these following commands :

```
cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && sudo python -m pip install .
```

6. After no error detected, run **``python app.py``** and flask server will start automatically.

## Credits

Thank you [theAIGuysCode](https://github.com/theAIGuysCode/yolov4-custom-functions). We edit the code and add another object detection to fit our purpose. 
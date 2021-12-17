import os

MODEL_NAME = 'charlie_detect_v4'     
MIN_SCORE_THRESHOLD = 0.2

DATA_DIR = os.path.join(os.getcwd(), 'data')
MODELS_DIR = os.path.join(DATA_DIR, 'models')

PATH_TO_CKPT = os.path.join(MODELS_DIR, os.path.join(MODEL_NAME, 'checkpoint/'))
PATH_TO_CFG = os.path.join(MODELS_DIR, os.path.join(MODEL_NAME, 'pipeline.config'))

LABEL_FILENAME = 'label_map.pbtxt'
PATH_TO_LABELS = os.path.join(MODELS_DIR, os.path.join(MODEL_NAME, LABEL_FILENAME))

# %%
# Load the model                                                                        

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import config_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(PATH_TO_CFG)
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(PATH_TO_CKPT, 'ckpt-0')).expect_partial()

@tf.function
def detect_fn(image):
    #Detect objects in image

    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)

    return detections, prediction_dict, tf.reshape(shapes, [-1])


# %%
# Load label map data (for plotting)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Label maps correspond index numbers to category names, so that when our convolution network
# predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility
# functions, but anything that returns a dictionary mapping integers to appropriate string labels
# would be fine.
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)

# %%
# Define the video stream
# ~~~~~~~~~~~~~~~~~~~~~~~
# We will use `OpenCV <https://pypi.org/project/opencv-python/>`_ to capture the video stream
# generated by our webcam. For more information you can refer to the `OpenCV-Python Tutorials <https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#capture-video-from-camera>`_
import cv2

# cap = cv2.VideoCapture(1) 
videocaputure_url = "http://192.168.2.64:8080/stream/video.mjpeg"
cap = cv2.VideoCapture(videocaputure_url) 

# %%
# Putting everything together
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The code shown below loads an image, runs it through the detection model and visualizes the
# detection results, including the keypoints.
#
# Note that this will take a long time (several minutes) the first time you run this code due to
# tf.function's trace-compilation --- on subsequent runs (e.g. on new images), things will be
# faster.
#
# Here are some simple things to try out if you are curious:
#
# * Modify some of the input images and see if detection still works. Some simple things to try out here (just uncomment the relevant portions of code) include flipping the image horizontally, or converting to grayscale (note that we still expect the input image to have 3 channels).
# * Print out `detections['detection_boxes']` and try to match the box locations to the boxes in the image.  Notice that coordinates are given in normalized form (i.e., in the interval [0, 1]).
# * Set ``min_score_thresh`` to other values (between 0 and 1) to allow more detections in or to filter out more detections.
import numpy as np
from time import time,sleep
from math import floor
import requests
from json import dumps
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
last_update = time() +15

while True:
    # Read frame from camera
    ret, frame = cap.read()
    image_np = np.array(frame)

    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)

    # Things to try:
    # Flip horizontally
    # image_np = np.fliplr(image_np).copy()

    # Convert image to grayscale
    # image_np = np.tile(
    #     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections, predictions_dict, shapes = detect_fn(input_tensor)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
          image_np_with_detections,
          detections['detection_boxes'][0].numpy(),
          (detections['detection_classes'][0].numpy() + label_id_offset).astype(int),
          detections['detection_scores'][0].numpy(),
          category_index,
          use_normalized_coordinates=True,
          max_boxes_to_draw=25,
          min_score_thresh=MIN_SCORE_THRESHOLD,
          agnostic_mode=False)

    # Display output
    # https://stackoverflow.com/questions/48915003/get-the-bounding-box-coordinates-in-the-tensorflow-object-detection-api-tutorial
    box = detections['detection_boxes'][0][0].numpy()
    #print(detections['detection_boxes'])
    center = ((box[3]-box[1])/2+box[1],(box[2]-box[0])/2+box[0])
    #print(img.shape)
    #print(center)
    #

    #print(detections['detection_scores'][0][0].numpy())
    if detections['detection_scores'][0][0].numpy()>MIN_SCORE_THRESHOLD:
        if abs(center[0]-0.5)>0.1:
            color = (0,0,255)
            s = requests.Session()
            retry = Retry(connect = 5, backoff_factor = 1)
            adapter = HTTPAdapter(max_retries = retry)
            s.mount('http://', adapter)
            s.keep_alive = False
            if center[0]>0.5:
                if last_update + 30 < time():
                    url = 'http://charlie.local/receiver'
                    myobj = {"direction": 3, "speed": 1, "AI": 1}
                    data = dumps(myobj)
                    x = s.post(url, json = data)
                    print("right")
            elif center[0]<0.5:
                if last_update + 30 < time():
                    url = 'http://charlie.local/receiver'
                    myobj = {"direction": 1, "speed": 1, "AI": 1}
                    data = dumps(myobj)
                    x = s.post(url, json = data)
                    print("left")
            cap.release()
            cap = cv2.VideoCapture(videocaputure_url) 
        else:
            color = (0,128,0)
        cv2.circle(image_np_with_detections,(floor(center[0]*frame.shape[1]),floor(center[1]*frame.shape[0])),5,color,-1)
    cv2.imshow('object detection',  cv2.resize(image_np_with_detections, (800, 600)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
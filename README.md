# VAH_Solution

# VAH.py

## __Important !!!__
### *Actually my program use only the camera 0 and 2 that means it can only run using the camera filming the goals area on each side of the playground.*
## Installation

### Dependencies

All Dependencies can be install using a virtual environment or be installed in
a standard environment.

#### Opencv

My program uses the last version of Opencv.
To install Opencv read the documentation from the official web site of [Opencv](https://opencv.org/opencv-3-4-1.html).

#### Tensorflow

The program uses Tensorflow 1.3 you can install it from the [official](https://www.tensorflow.org/install/) web site.
You can also install it from pip using but that will install the last version:

    $> pip3 tensorflow

#### Others

The program uses the last version of Numpy, Argparse and Scikit-image.

    $> pip3 install numpy
    $> pip3 install argparse
    $> pip3 install -U scikit-image

## Executing

To run, my program need some details:
- The camera address or videos (use __-i__ to specify it)
- The model directory (use __-d__ to specify it)

if you want to change the name of the final video you can use __-n__ to change
it.

I suppose that the model is in the same directory and his name is **Model_VAH**.
Some examples to run my program:

    python3 ./VAH -h

To display the help.

    python3 ./VAH -i 0.mp4 1.mp4 -d ./Model_VAH/

Run the program on the video *0.mp4* and *2.mp4* using the model in
__Model_VAH__.

    python3 ./VAH -i http://camera0 http://camera2 -d ./Model_VAH/

Run the program on the video *http://camera0* and *http://camera2* using the
model in __Model_VAH__. This part is in testing some issues can be find...

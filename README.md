# Face Recognition Video Stream Project Using Python

## Overview

This project implements real-time face recognition using OpenCV and the face_recognition library. It captures video from the default camera, detects faces, and recognizes known individuals based on pre-loaded images.


## Features

Real-time face detection and recognition.

Support for multiple known faces.

Visual feedback with bounding boxes and labels around detected faces.

Handles cases where no faces are detected.


## Requirements

To run this project, you'll need the following libraries:

Python 3.x

OpenCV

face_recognition

NumPy


## SetUp

Clone the repository

Add your own knwon images - in JPEG format.


## How it works

The script loads known images and extracts face encodings.

It initializes a video stream from the default camera.

For every frame captured:

  The frame is resized to speed up processing.
  
  Face locations and encodings are detected.
  
  Detected faces are compared with known faces.
  
  Results are displayed with bounding boxes and labels.


## Usage

The application will display a video window showing the camera feed.

Detected faces will be labeled with names based on the known images.

Press the q key to exit the application.


## TroubleShooting

Ensure your camera is functioning correctly.

Check if the known images are correctly placed and formatted.

If no faces are detected, try adjusting the lighting and position relative to the camera.


## License

Distributed under the MIT License.


## Acknowledgments

OpenCV

face_recognition

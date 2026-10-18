
# OpenCV Basics

A collection of beginner-level Python experiments exploring **computer vision and image processing with OpenCV**. This repository documents my hands-on learning of image manipulation, video capture, colour spaces, image filtering, perspective transformation and real-time webcam processing.

## Overview

The goal of this repository is to understand the fundamentals of computer vision by implementing small Python programs and experimenting with OpenCV's image-processing functions.

Rather than focusing on one large application, the repository is organised as a collection of independent scripts, each exploring a specific concept or technique.

## Concepts Covered

- **Image and Video Processing** — Reading and displaying images, loading video files and capturing webcam footage.
- **Image Transformations** — Resizing, cropping, and perspective transformation.
- **Image Filtering** — Grayscale conversion, Gaussian blur, Canny edge detection, dilation and erosion.
- **Drawing with OpenCV** — Drawing lines, rectangles and circles, and adding text to images or live video frames.
- **HSV Colour Detection** — Working with HSV colour ranges, trackbars and colour masks.
- **Real-Time Webcam Processing** — Manipulating live camera frames, resizing frames and displaying graphical overlays.

## Repository Structure

| File | Main concept |
|---|---|
| `1.py` | Image, video and webcam input |
| `2.py` | Image resizing |
| `3.py` | Grayscale conversion, blurring, edge detection, dilation and erosion |
| `4.py` | Creating an image and drawing shapes |
| `5.py` | Perspective transformation |
| `6,7.py` | Interactive trackbars and HSV colour-range selection |
| `8.py` | Image resizing and cropping |
| `9.py` | Webcam frame resizing, rotation and quadrant arrangement |
| `10.py` | Drawing shapes and text on a live webcam feed |
| `11.py` | HSV colour detection with webcam input |

Each script is intended to be explored independently. Some experiments may require small adjustments depending on the available images, videos, or webcam.

## Tech Stack

- **Python 3**
- **OpenCV** (`opencv-python`)
- **NumPy**

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NeelManiar/OpenCV-Basics.git
cd OpenCV-Basics
```

### 2. Install the dependencies

```bash
pip install opencv-python numpy
```

### 3. Run an experiment

Choose an individual Python file and run it:

```bash
python 3.py
```

Replace `3.py` with the script you want to explore.

## Requirements

- Python 3 installed on your system.
- OpenCV and NumPy installed.
- A webcam for experiments involving live camera input.
- The relevant image or video files for scripts that load external media.

**Note:** Some scripts reference files such as `Sam-Banner.png`, `cards.jpeg` and `Youtube Intro.mp4`. Ensure these files are available in the expected working directory, or update their paths before running those scripts.

The scripts use OpenCV's graphical display functions, such as `cv2.imshow()`, so a local Python environment with desktop-window support is recommended.

## Future Improvements

- Organise scripts into topic-based folders with descriptive filenames.
- Add visual examples and explanations of each operation.
- Improve input validation and error handling.
- Expand colour segmentation and contour-detection experiments.
- Build a complete computer-vision project using the concepts explored here.

---

**Author:** [Neel Maniar](https://github.com/NeelManiar)

**Repository:** [OpenCV-Basics](https://github.com/NeelManiar/OpenCV-Basics)

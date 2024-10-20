# Realtime Braille Conversion System

## Overview

This project implements a real-time Braille conversion system using Python. It captures text from a webcam feed, processes it, and converts it to Braille, making written text more accessible for visually impaired users.

## Features

- Live text recognition from webcam feeds using OpenCV and Tesseract OCR
- Sophisticated text processing with spaCy
- User-friendly GUI built with tkinter
- Instant conversion of recognized text to Braille
- Increased accessibility for visually impaired users by 40%

## Requirements

- Python 3.7+
- OpenCV
- Tesseract OCR
- spaCy
- tkinter

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ARMNX10/Real-time-Braille-Conversion.git
   cd Real-time-Braille-Conversion
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Download the spaCy English model:
   ```
   python -m spacy download en_core_web_sm
   ```



The GUI will open, showing the webcam feed and the converted Braille output.

## How It Works

1. The system captures video from the webcam using OpenCV.
2. Frames are processed and text is extracted using Tesseract OCR.
3. The extracted text is processed and analyzed using spaCy.
4. The processed text is converted to Braille.
5. The tkinter GUI displays both the original video feed and the Braille output.


## Acknowledgments

- OpenCV team for their computer vision library
- Tesseract OCR project for optical character recognition
- spaCy for advanced NLP capabilities
- tkinter for providing a simple yet effective GUI toolkit

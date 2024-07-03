import json
from process_image import ImageProcessor
import cv2
import mediapipe as mp
import numpy as np



if __name__ == '__main__':

    # Trainer pose
    image_processor = ImageProcessor()
    image_processor.process_images("Virabhadrasana.jpg")
    image_processor.calculate_angle()
    image_processor.display_angle_list()

    # trainee pose
    image_processor2 = ImageProcessor()
    image_processor2.process_images("Virabhadrasana2.jpg")
    image_processor2.calculate_angle()
    image_processor2.display_angle_list()

    # compare 2 images
    if image_processor == image_processor2:
        print("Image processor match")

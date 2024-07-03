import cv2
import mediapipe as mp
from calculate_angle import calculate_angle
from pose_constants import body_parts
import numpy as np


# this class process image. this class has 3 objects "coordinates_list", "angle_list", and "content_list".
#
# . Flow chart
# 1. Function "process_images" Use mediaPipe and CV2 to read image and get landmark's coordinates, then put all coordinates into coordinates_list
# 2.

class ImageProcessor:
    def __init__(self):
        self.coordinates_list = None
        self.angle_list = []  # First list for store angle
        self.content_list = []  # Second list for store content

    def process_images(self, image_path):
        # Load image from file
        image = cv2.imread(image_path)

        # Convert BGR image to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_pose = mp.solutions.pose
        pose_landmark = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # Process the image and get pose landmarks
        results = pose_landmark.process(rgb_image)

        if results.pose_landmarks:
            # Draw landmarks on the image (optional)
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Save the modified image (you can customize this part)
            cv2.imwrite("output_{}".format(image_path), image)

            # return The results contains both normalized coordinates (Landmarks) and world coordinates (WorldLandmarks) for each landmark
            self.coordinates_list = results
        else:
            return None

    def calculate_angle(self):
        if self.coordinates_list is not None:
            landmarks = self.coordinates_list.pose_landmarks.landmark
            for body_part in body_parts:
                point_a = np.array([landmarks[list(body_part.keys())[0]].x,
                                    landmarks[list(body_part.keys())[0]].y,
                                    landmarks[list(body_part.keys())[0]].z])

                point_b = np.array([landmarks[list(body_part.keys())[1]].x,
                                    landmarks[list(body_part.keys())[1]].y,
                                    landmarks[list(body_part.keys())[1]].z])

                point_c = np.array([landmarks[list(body_part.keys())[2]].x,
                                    landmarks[list(body_part.keys())[2]].y,
                                    landmarks[list(body_part.keys())[2]].z])

                angle_degree = calculate_angle(point_a, point_b, point_c)
                data_string = (f"Angle between {body_part[list(body_part.keys())[0]]}, "
                               f"{body_part[list(body_part.keys())[1]]}, "
                               f"and {body_part[list(body_part.keys())[2]]}: {angle_degree:.2f} degrees")
                self.content_list.append(data_string)
                self.angle_list.append(angle_degree)

    def display_angle_list(self):
        if len(self.angle_list) != 0:
            for angle in self.angle_list:
                print(f"{angle:.2f}")

    def display_content_list(self):
        if len(self.content_list) != 0:
            for content in self.content_list:
                print(content)

    def display_coordinates_list(self):
        if self.coordinates_list is not None:
            landmarks = self.coordinates_list.pose_landmarks.landmark
            for landmark in landmarks:
                print(f"{landmark.x}, {landmark.y}, {landmark.z}")
                """
            print(landmarks[0])
            print(landmarks[1])
            print(landmarks[0].x)
            print(landmarks[1].y)
            print(type(landmarks))
            print(len(landmarks))
"""
    def __eq__(self, second_image_processor):
        # return self.coordinates_list.pose_landmarks.landmark == second_image_processor.coordinates_list.pose_landmarks.landmark
        if set(self.angle_list) == set(second_image_processor.angle_list):
            return True
        else:
            return False

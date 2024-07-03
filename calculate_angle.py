import numpy as np


# This function will calculate angle based on 3  3D coordinates
# Set B is center point

def calculate_angle(a, b, c):
    # Calculate vectors from B to A and B to C
    ba = a - b
    bc = c - b

    # Calculate the cosine of the angle
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))

    # Convert the cosine to radians
    angle_radians = np.arccos(cosine_angle)

    # Convert radians to degrees
    angle_degrees = np.degrees(angle_radians)

    return angle_degrees

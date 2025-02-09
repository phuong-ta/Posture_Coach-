# Mediapipe tracks 33 body landmark locations. 
# Because this project is used to detect human pose, so all landmark locations from head will removed.
# From 22 body landmark locations to get 14 angles
# This list is used to store data values
# key is landmark id number ()
# value is humand landmark name

body_parts = [
    {11: 'left shoulder', 13: 'left elbow', 15: 'left wrist'},
    {12: 'right shoulder', 14: 'right elbow', 16: 'right wrist'},
    {13: 'left elbow', 11: 'left shoulder', 12: 'right shoulder'},
    {14: 'right elbow', 12: 'right shoulder', 11: 'left shoulder'},
    {14: 'right elbow', 12: 'right shoulder', 24: 'right hip'},
    {13: 'left elbow', 11: 'left shoulder', 23: 'left hip'},
    {12: 'right shoulder', 24: 'right hip', 26: 'right knee'},
    {11: 'left shoulder', 23: 'left hip', 25: 'left knee'},
    {23: 'left hip', 24: 'right hip', 26: 'right knee'},
    {24: 'right hip', 23: 'left hip', 25: 'left knee'},
    {24: 'right hip', 26: 'right knee', 28: 'right ankle'},
    {23: 'left hip', 25: 'left knee', 27: 'left ankle'},
    {26: 'right knee', 28: 'left ankle', 32: 'right foot index'},
    {25: 'left knee', 27: 'left ankle', 31: 'left foot index'}
]
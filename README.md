# PostureCoach: AI-Powered Posture Improvement App


## Overview
PostureCoach is an innovative AI application designed to help sports enthusiasts practice correct posture during their training sessions. Whether you’re into yoga, weightlifting, or any other sport, PostureCoach ensures that you maintain optimal form for better performance and injury prevention.

## Features
1. Pose Detection and Comparison:
+ Utilizes MediaPipe to detect key landmarks on the human body from uploaded photos or videos.
+ Calculates angles between detected poses.
+ Compares user’s posture with reference poses.
2. Real-Time Feedback:
+ LLama 3 provides expert feedback based on different angles.
+ Offers corrective instructions to improve posture.
3. Text-to-Speech (TTS) Integration:
+ Uses another AI model for direct audio feedback.
+ Converts text-based feedback into lifelike spoken audio.
## How It Works
1. Upload Reference Media:
Users upload photos or videos of correct posture they want to emulate.
2. Practice and Record:
Users record their own practice sessions.
Upload corresponding media to the app.
3. Real-Time Analysis:
PostureCoach analyzes user’s posture during practice.
Compares it to reference poses.
4. Feedback Loop:
LLama 3 evaluates angles and provides feedback.
TTS model converts feedback to spoken instructions.
## Flow Chart
1. Detect 33 landmarks of human bodies to get 33 3D coordinates.
2. Use coordinates to calculate 14 angles from each betwend 3 landmarks of human bodies.
3. Compare trainee and trainer angles to find diffireance.
4. give feedback.
## Getting Started
1. Clone the Repository:
+ git clone https://github.com/yourusername/PostureCoach.git

2. Install Dependencies:
+ pip install mediapipe.
+  pip install opencv

3. Run the App:
+ Add trainee and trainer'exercise pose
+ modify image path
+ run app
+ check diffirence 
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
How It Works
Upload Reference Media:
Users upload photos or videos of correct posture they want to emulate.
Practice and Record:
Users record their own practice sessions.
Upload corresponding media to the app.
Real-Time Analysis:
PostureCoach analyzes user’s posture during practice.
Compares it to reference poses.
Feedback Loop:
LLama 3 evaluates angles and provides feedback.
TTS model converts feedback to spoken instructions.
Getting Started
Clone the Repository:
git clone https://github.com/yourusername/PostureCoach.git

Install Dependencies:
pip install -r requirements.txt

Run the App:
python app.py

Usage
Upload Reference Media:
Add reference photos or videos to the app.
Record Your Practice:
Record your practice session.
Upload your practice media.
Receive Feedback:
PostureCoach analyzes your posture.
LLama 3 provides feedback.
TTS model speaks the instructions.
Acknowledgments
Thanks to the open-source community for providing the tools and models used in this project.
License
This project is licensed under the MIT License - see the LICENSE file for details.
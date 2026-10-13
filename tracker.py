import cv2
import os
import urllib.request
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandTracker:
    def __init__(self):
        model_path = 'hand_landmarker.task'
        if not os.path.exists(model_path):
            print("Downloading modern MediaPipe model (this only happens once)...")
            url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
            urllib.request.urlretrieve(url, model_path)
            print("Download complete!")

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_hands=1
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.mp_image_format = mp.ImageFormat.SRGB

    def find_hands(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=self.mp_image_format, data=rgb_frame)
        self.results = self.detector.detect(mp_image)

        if self.results.hand_landmarks:
            for hand_landmarks in self.results.hand_landmarks:
                h, w, _ = frame.shape
                for idx in [8, 12, 16, 20]:
                    tip = hand_landmarks[idx]
                    joint = hand_landmarks[idx - 2]
                    cv2.circle(frame, (int(tip.x * w), int(tip.y * h)), 8, (0, 255, 0), -1)
                    cv2.circle(frame, (int(joint.x * w), int(joint.y * h)), 6, (0, 0, 255), -1)
        return frame

    def get_gesture(self):
        if not hasattr(self, 'results') or not self.results.hand_landmarks:
            return "neutral"

        hand_landmarks = self.results.hand_landmarks[0]
        tip_ids = [8, 12, 16, 20]
        joint_ids = [6, 10, 14, 18]

        up_fingers = 0
        for i in range(4):
            if hand_landmarks[tip_ids[i]].y < hand_landmarks[joint_ids[i]].y:
                up_fingers += 1

        if up_fingers >= 3:
            return "accelerate"
        elif up_fingers == 2:
            return "restart"  # NEW: Peace sign triggers restart
        elif up_fingers == 0:
            return "brake"
        else:
            return "neutral"  # 1 finger is now a safe "neutral" buffer zone
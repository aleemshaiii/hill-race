import cv2
import pyautogui
from tracker import HandTracker

pyautogui.FAILSAFE = False

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    
    current_key = None

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame = tracker.find_hands(frame)
        gesture = tracker.get_gesture()

        # 1. Accelerate
        if gesture == "accelerate":
            if current_key != "right":
                if current_key is not None: pyautogui.keyUp(current_key)
                pyautogui.keyDown("right")
                current_key = "right"
            cv2.putText(frame, "GAS (Right Arrow)", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 2. Brake
        elif gesture == "brake":
            if current_key != "left":
                if current_key is not None: pyautogui.keyUp(current_key)
                pyautogui.keyDown("left")
                current_key = "left"
            cv2.putText(frame, "BRAKE (Left Arrow)", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        
        # 3. Restart (NEW)
        elif gesture == "restart":
            if current_key != "enter":
                if current_key is not None: pyautogui.keyUp(current_key)
                pyautogui.press("enter")  # .press() taps it once, doesn't hold it
                current_key = "enter"
            cv2.putText(frame, "RESTART (Enter)", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        # 4. Neutral
        else:
            if current_key is not None:
                pyautogui.keyUp(current_key)
                current_key = None
            cv2.putText(frame, "NEUTRAL (Coast)", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.imshow("Hill Climb Vision Controller", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if current_key:
        pyautogui.keyUp(current_key)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
 # GitHub UI test successful   
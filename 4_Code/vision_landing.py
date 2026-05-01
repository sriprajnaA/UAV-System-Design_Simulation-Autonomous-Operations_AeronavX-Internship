import cv2
import numpy as np

print("Vision-Based Landing System Started...")

# Try webcam, else use test image
cap = cv2.VideoCapture(0)
USE_TEST_IMAGE = not cap.isOpened()

def detect_landing_pad(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    # Detect green landing pad
    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
   
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    frame_center_x = frame.shape[1] // 2
    frame_center_y = frame.shape[0] // 2
   
    cv2.drawMarker(frame, (frame_center_x, frame_center_y),
                  (255, 0, 0), cv2.MARKER_CROSS, 20, 2)
   
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            pad_center_x = x + w // 2
            pad_center_y = y + h // 2
           
            error_x = pad_center_x - frame_center_x
            error_y = pad_center_y - frame_center_y
           
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.drawMarker(frame, (pad_center_x, pad_center_y),
                          (0, 255, 0), cv2.MARKER_CROSS, 20, 2)
            cv2.putText(frame, f"LANDING PAD FOUND", (x, y-30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Error X: {error_x}px Y: {error_y}px",
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
           
            print(f"Landing pad detected! Error X: {error_x}px, Y: {error_y}px")
           
            if abs(error_x) < 20 and abs(error_y) < 20:
                print("ALIGNED! Initiating landing sequence...")
                cv2.putText(frame, "ALIGNED - LANDING!", (50, 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            else:
                print(f"Adjusting position... moving {'right' if error_x > 0 else 'left'} and {'forward' if error_y > 0 else 'backward'}")
           
            return True, frame, error_x, error_y
   
    print("Searching for landing pad...")
    return False, frame, 0, 0

if USE_TEST_IMAGE:
    print("No webcam, generating test frame...")
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    # Draw green landing pad
    cv2.rectangle(frame, (280, 200), (380, 300), (0, 255, 0), -1)
    cv2.circle(frame, (330, 250), 30, (0, 200, 0), -1)
    detected, result, ex, ey = detect_landing_pad(frame)
    cv2.imwrite("landing_test_result.png", result)
    print(f"Landing pad detected: {detected}")
    print(f"Landing error - X: {ex}px, Y: {ey}px")
    print("Result saved as landing_test_result.png")
else:
    print("Press Q to quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detected, result, ex, ey = detect_landing_pad(frame)
        cv2.imshow("Vision Landing System", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

print("Vision landing system complete!")

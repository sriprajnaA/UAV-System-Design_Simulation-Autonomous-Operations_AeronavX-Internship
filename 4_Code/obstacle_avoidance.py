import cv2
import numpy as np

print("Starting obstacle detection...")

# Simulated camera feed (webcam or test image)
cap = cv2.VideoCapture(0)

# If no webcam, use a test image instead
USE_TEST_IMAGE = not cap.isOpened()

def detect_obstacle(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    # Detect red obstacles
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
   
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "OBSTACLE DETECTED", (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("Obstacle detected! Triggering avoidance maneuver...")
            print("Action: Moving sideways to avoid obstacle")
            return True, frame
    return False, frame

if USE_TEST_IMAGE:
    print("No webcam found, generating test frame...")
    # Create a test frame with a red rectangle (simulated obstacle)
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.rectangle(frame, (200, 150), (400, 350), (0, 0, 255), -1)
    detected, result = detect_obstacle(frame)
    cv2.imwrite("obstacle_test_result.png", result)
    print(f"Obstacle detected: {detected}")
    print("Result saved as obstacle_test_result.png")
else:
    print("Press Q to quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detected, result = detect_obstacle(frame)
        cv2.imshow("Obstacle Detection", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

print("Obstacle detection complete!")

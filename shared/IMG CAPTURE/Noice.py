import cv2
import os
import time

# Camera index 1 for an external camera
camera_index = 0

# Initialize the webcam
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Could not open the external camera.")
else:
    # Create a window to display the webcam feed
    cv2.namedWindow("Webcam Feed", cv2.WINDOW_NORMAL)

    # Read and display the webcam feed for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 10:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Webcam Feed", frame)
            cv2.waitKey(1)  # Refresh the display

    # Capture a single frame after 10 seconds
    ret, frame = cap.read()

    if ret:
        # Define the file path where you want to save the captured image
        image_path = "Image1.jpg"

        # Delete the existing image if it exists
        if os.path.exists(image_path):
            os.remove(image_path)

        # Save the captured frame as an image
        cv2.imwrite(image_path, frame)

        print(f"Image captured and saved as {image_path}")

    # Release the webcam and close the window
    cap.release()
    cv2.destroyWindow("Webcam Feed")

# Close all OpenCV windows (if any)
cv2.destroyAllWindows()

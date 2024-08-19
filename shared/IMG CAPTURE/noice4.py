import cv2
import os
import time
import pytesseract
from pytesseract import Output

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Camera index 1 for an external camera
camera_index = 1

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

        # Crop the captured image
        cropped_image = frame[100:400, 200:600]  # Adjust the coordinates as needed
        cropped_image_path = "Image2.jpg"

        # Delete the existing cropped image if it exists
        if os.path.exists(cropped_image_path):
            os.remove(cropped_image_path)

        # Save the cropped image
        cv2.imwrite(cropped_image_path, cropped_image)

        print(f"Cropped image saved as {cropped_image_path}")

        # Perform OCR on the cropped image with additional parameters
        custom_config = r'--oem 3 --psm 7'
        extracted_text = pytesseract.image_to_string(cropped_image_path, config=custom_config, output_type=Output.STRING)

        # Define the file path for the output text file
        output_file_path = "Output.txt"

        # Write the extracted text to the output text file
        with open(output_file_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        print(f"Extracted text saved in {output_file_path}")

    # Release the webcam and close the window
    cap.release()
    cv2.destroyWindow("Webcam Feed")

# Close all OpenCV windows (if any)
cv2.destroyAllWindows()

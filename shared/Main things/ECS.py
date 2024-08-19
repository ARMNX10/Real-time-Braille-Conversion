import cv2
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(1)

# Open a text file for writing in overwrite mode
output_file = open("Output.txt", "w")

text_detected = False
start_time = time.time()
detection_duration = 20# Duration in seconds
last_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply image preprocessing (resize, denoise, and enhance contrast) as needed
    # gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # gray = cv2.equalizeHist(gray)

    # Use additional configuration parameters to improve font recognition
    config = '--psm 6'  # You can try different PSM modes and other parameters

    text = pytesseract.image_to_string(gray, config=config)

    if text.strip():
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        text_detected = True
        last_text = text  # Save the last detected text
    elif text_detected and (time.time() - start_time) >= detection_duration:
        break

    cv2.imshow('Text Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Write the last detected text to the output file in overwrite mode
output_file.write(last_text)

# Close the output file
output_file.close()

cap.release()
cv2.destroyAllWindows()

import cv2
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(0)

# Open a text file for writing in overwrite mode
output_file = open("Output.txt", "w")

text_detected = False
start_time = time.time()
detection_duration = 15 # Duration in seconds
last_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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

# Integration of text processing to save refined text in "Output2.txt"
input_file = open("Output.txt", "r")
output_file2 = open("Output2.txt", "w")

# Read the content of "Output.txt"
input_text = input_file.read()
input_file.close()

# Define a function to clean and extract distinguishable characters
def clean_text(input_text):
    # Define the characters to keep
    valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    # Initialize an empty string to store the cleaned text
    cleaned_text = ""

    # Flag to exclude characters after a question mark
    exclude_text = False

    for char in input_text:
        if char == "?":
            exclude_text = True
        if not exclude_text and char in valid_characters:
            cleaned_text += char

    return cleaned_text

# Clean and extract distinguishable characters from the text
cleaned_text = clean_text(input_text)

# Write the cleaned text to "Output2.txt"
output_file2.write(cleaned_text)
output_file2.close()

cap.release()
cv2.destroyAllWindows()

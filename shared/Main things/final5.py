import cv2
import pytesseract
import time
import collections
import spacy

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Open a text file for writing in overwrite mode
output_file = open("Output.txt", "w")

# List to store all detected responses, including garbage
all_responses = []

cap = cv2.VideoCapture(1)

text_detected = False
start_time = time.time()
detection_duration = 10  # Duration in seconds
last_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    elapsed_time = time.time() - start_time  # Calculate elapsed time

    if elapsed_time >= detection_duration:
        break  # Close the loop if the specified duration is reached

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use additional configuration parameters to improve font recognition
    config = '--psm 6'

    text = pytesseract.image_to_string(gray, config=config)

    if text.strip():
        all_responses.append(text)  # Store all responses, including garbage
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        text_detected = True
        last_text = text  # Save the last detected text

    cv2.imshow('Text Recognition', frame)

# Write all detected responses, including garbage, to the output file in "Output.txt"
output_file.write('\n'.join(all_responses))
output_file.close()

# Find the most common response (without garbage)
filtered_responses = [response for response in all_responses if not response.isspace()]
response_count = collections.Counter(filtered_responses)
most_common_response = response_count.most_common(1)
if most_common_response:
    most_common_response_text, _ = most_common_response[0]

    # Write the most common response (without garbage) to "Output2.txt"
    with open("Output2.txt", "w") as output_file2:
        output_file2.write(most_common_response_text)

    # Define a function to clean and filter meaningful words
    def filter_meaningful_words(text):
        doc = nlp(text)
        meaningful_words = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "GPE"]]
        meaningful_words.extend([token.text for token in doc if token.is_alpha])
        return ' '.join(meaningful_words)

    # Filter meaningful words from the most common response (without garbage)
    meaningful_response = filter_meaningful_words(most_common_response_text)

    # Write the filtered response to "Output3.txt"
    with open("Output3.txt", "w") as output_file3:
        output_file3.write(meaningful_response)

cap.release()
cv2.destroyAllWindows()

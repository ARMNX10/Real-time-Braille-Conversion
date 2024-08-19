import cv2
import pytesseract
import time
import collections
import spacy
import subprocess
import atexit


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

nlp = spacy.load("en_core_web_sm")

output_file = open("Output.txt", "w")
output_file3 = open("Output3.txt", "w")  

all_responses = []
meaningful_responses = []  

cap = cv2.VideoCapture(0)

text_detected = False
start_time = time.time()
detection_duration = 20  
last_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    config = '--psm 6'

    text = pytesseract.image_to_string(gray, config=config)

    if text.strip():
        all_responses.append(text)
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        text_detected = True
        last_text = text

    if text_detected and (time.time() - start_time) >= detection_duration:
        break  

    cv2.imshow('Text Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output_file.write('\n'.join(all_responses))
output_file.close()

filtered_responses = [response for response in all_responses if not response.isspace()]
response_count = collections.Counter(filtered_responses)
most_common_response = response_count.most_common(1)
if most_common_response:
    most_common_response_text, _ = most_common_response[0]

    with open("Output2.txt", "w") as output_file2:
        output_file2.write(most_common_response_text)

    def filter_meaningful_words(text):
        doc = nlp(text)
        meaningful_words = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "GPE"]]
        meaningful_words.extend([token.text for token in doc if token.is_alpha])
        return ' '.join(meaningful_words)

    meaningful_response = filter_meaningful_words(most_common_response_text)

    if meaningful_response: 
        meaningful_responses.append(meaningful_response)

output_file3.write('\n'.join(meaningful_responses))  
output_file3.close()


output_file4 = open("Output4.txt", "w")

with open("Output3.txt", "r") as output_file3:
    content = output_file3.read().replace('\n', '')  

    
    modified_content = ' '.join(list(content))
    output_file4.write("   ")
    output_file4.write(modified_content)

output_file4.close()

cap.release()
cv2.destroyAllWindows()
def run_nice_script():
    subprocess.run(['python', 'nice.py'])

atexit.register(run_nice_script)










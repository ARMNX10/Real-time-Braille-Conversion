import cv2

cap = cv2.VideoCapture(0)  # Change to the video file path if you want to record from a file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
frame_count = 0
capture_frame = None

while True:
    ret, frame = cap.read()
    out.write(frame)
    frame_count += 1

    if frame_count == 29 * 30:  # Assuming 30 frames per second
        capture_frame = frame
        print("Captured frame at 29th second")

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit the loop
        break

# Save the captured frame as a PNG image
if capture_frame is not None:
    cv2.imwrite('captured_frame.png', capture_frame)
    print("Captured frame saved as captured_frame.png")

# Release video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()

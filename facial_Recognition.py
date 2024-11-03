import cv2
import face_recognition
import numpy as np
import os

# Load multiple known images and learn how to recognize them
known_images = [] # Insert your images here

known_face_encodings = []
known_face_names = [os.path.splitext(os.path.basename(image))[0] for image in known_images]  # Get filenames without extensions

for image in known_images:
    try:
        # Load the image using face_recognition
        img = face_recognition.load_image_file(image)

        # Get face encodings
        encodings = face_recognition.face_encodings(img)
        if encodings:  # Check if any encodings were found
            known_face_encodings.append(encodings[0])
        else:
            print(f"No faces found in image '{image}'.")

    except Exception as e:
        print(f"Error processing image '{image}': {e}")

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Open a video capture object
video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()

    if not ret:
        print("Error: Unable to capture video.")
        break

    # Resize the frame to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (OpenCV) to RGB color (face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]
        
    code = cv2.COLOR_BGR2RGB
    rgb_small_frame = cv2.cvtColor(rgb_small_frame, code)

    # Only process every other frame to save time
    if process_this_frame:
        # Find all face locations in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)

        # Check if any face locations were found
        if face_locations:
            # Get face encodings for the detected faces
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        else:
            face_encodings = []

        face_names = []
        for face_encoding in face_encodings:
            # Check if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            if matches:
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame was resized
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with the filename below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()

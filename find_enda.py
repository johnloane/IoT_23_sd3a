from PIL import Image, ImageDraw
import numpy as np

import face_recognition

known_face = face_recognition.load_image_file("enda.jpg")
encoding = face_recognition.face_encodings(known_face)[0]
unknown_image = face_recognition.load_image_file("enda_group.jpg")
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)
for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([encoding], face_encodings)
    face_distances = face_recognition.face_distance([encoding], face_encodings)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        draw.rectangle(((left-20, top-20), (right+20, bottom+20)), 
                       outline=(0, 255, 0), width=20)
del draw
pil_image.show()
import face_recognition

whin = face_recognition.load_image_file("whinderson.png")
whin_encoding = face_recognition.face_encodings(whin)[0]

for i in range(0, 4):
    unknown = face_recognition.load_image_file(f"{i}.png")
    unknown_encoding = face_recognition.face_encodings(unknown)[0]
    resultados = face_recognition.compare_faces([whin_encoding], unknown_encoding)
    if resultados[0] == True:
        print("E a foto do Whinderson")
    else:
        print("Nao e a foto do Whinderson")
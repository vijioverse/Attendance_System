import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import  storage
from firebase_admin import db

cred = credentials.Certificate("surveillance-and-attendance-firebase-adminsdk-tsrdn-050d9a2fb6.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://surveillance-and-attendance-default-rtdb.firebaseio.com/",
    'storageBucket':"surveillance-and-attendance.appspot.com"
})


folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
ref = db.reference("Character")

data = {

    "19":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "Derogatory": "Actress",
            "year": 1,
            "last_attendance_time": "2022-12-12 00:54:34"
        },
    "20":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "Derogatory": "Tech Giant",
            "year": 2,
            "last_attendance_time": "2022-12-10 00:54:34"
        },
"21":
    {
        "name": "Naorem",
        "starting_year": "2021",
        "Derogatory": "Engineer",
        "major": "Developer",
        "total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-04-27 00:54:34"
},
"10":
    {
        "name": "Jon Snow",
        "starting_year": "2022",
        "Derogatory": "The Bastard of Winterfell",
        "major": "Kingship",
        "total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},
    "2":
        {
        "name": "Daenerys Targaryen",
        "starting_year": "2021",
        "Derogatory": "Dragongirl",
        "major": "Fire",
        "total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
    },
    "16": {
        "name": "Lord Varys",
        "starting_year": "2022",
        "Derogatory": "The Spider",
        "major": "Flexibility",
        "total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
    },
    "17": {
        "name": "Cersei Lannister",
        "Derogatory": "Brotherfucker",
        "starting_year": "2022",
        "major": "Critical Thinking",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "14": {
        "name": "Sansa Stark",
        "starting_year": "2023",
        "Deroratory": "Little Bird",
        "major": "Adaptability",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "11": {
        "name": "Jaime Lannister",
        "starting_year": "2022",
        "Derogatory": "Kingslayer",
        "major": "Swordmanship",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "6": {
        "name": "Theon",
        "starting_year": "2022",
        "Derogatory": "Reek",
        "major": "Acher",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "5": {
        "name": "Arya Stark",
        "starting_year": "2022",
        "Derogatory": "Stick Boy",
        "major": "Assasination",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "4": {
        "name": "Jorah Mormont",
        "starting_year": "2023",
        "Derogatory": "Jorah the Andal",
        "major": "Bravery",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "8": {
        "name": "Davos Seaworth",
        "starting_year": "2024",
        "Derogatory": "Onion Knight",
        "major": "Smuggler",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "7": {
        "name": "Brienne of Tarth",
        "starting_year": "2024",
        "Derogatory": "The Maid of Tarth",
        "major": "Fighter",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},

    "3": {
        "name": "Bran Stark",
        "starting_year": "2023",
        "Derogatory": "Bran the Broken",
        "major": "Controlling Animals",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},
    "1": {
        "name": "Sandor Clegane",
        "starting_year": "2023",
        "Derogatory": "Dog",
        "major": "Axe",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},
    "13": {
        "name": "Bronn",
        "starting_year": "2023",
        "Derogatory": "Blackwater",
        "major": "Leadership",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},
    "12": {
        "name": "Tormund Giantbane",
        "starting_year": "2024",
        "Derogatory": "Husband of Bear",
        "major": "Courages",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
},
    "18": {
        "name": "Gendry Baratheon",
        "starting_year": "2024",
        "Derogatory": "The Bastard",
        "major": "Blacksmith",
"total_attendance": 7,
"year": 2,
        "last_attendance_time": "2024-02-11 00:54:34"
    }
}
for key, value in data.items():
    ref.child(key).set(value)
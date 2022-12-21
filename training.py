from sklearn.preprocessing import LabelEncoder
import os
import pickle
import cv2
import numpy as np
from PIL import Image


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = str(os.path.split(imagePath)[-1].split(".")[0])
        print(Id)
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def training():
    le = LabelEncoder()
    faces, Id = getImagesAndLabels("home/TrainingImage")
    Id = le.fit_transform(Id)
    output = open('label_encoder.pkl', 'wb')
    pickle.dump(le, output)
    output.close()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(Id))
    recognizer.save(r"home/Trained_Model/Trainner.yml")

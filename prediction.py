import cv2, os
import pickle
import pandas as pd
import numpy as np


def prediction():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read(r"home/Trained_Model\Trainner.yml")
    harcascadePath = r"home/Haarcascade\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    # df = pd.read_csv(r"Student_Details\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    # print(df)
    font = cv2.FONT_HERSHEY_SIMPLEX
    pkl_file = open('label_encoder.pkl', 'rb')
    le = pickle.load(pkl_file)
    pkl_file.close()
    data = pd.read_csv("home/person_details/person_details.csv")
    # print(data)
    # rollno=data['Id']
    val = str(data.Email.values)

    det = 0
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            # print(conf)
            if (conf < 50):
                det += 1
                tt = le.inverse_transform([Id])
                # print(type(tt))
                tt = tt[0]
                # print(tt)
                if det == 10:
                    return tt
            else:
                Id = 'Unknown'
                tt = str(Id)
                # print(tt)
            if (conf > 55):
                noOfFile = len(os.listdir("home/ImageUnknown")) + 1
                cv2.imwrite(r"home\ImageUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                # print(tt)
                # return tt
            # print("tt:",str(tt))
            # print("x:", str(x))
            # print("y:", str(y))
            # print("font:", str(font))

            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()

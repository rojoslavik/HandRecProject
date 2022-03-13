import cv2
from find_landmarks import HandDetector

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
handdetector = HandDetector()

while cap.isOpened():
    success, img = cap.read()
    handlandmarks = handdetector.find_landmarks(image=img, draw=True)

    if success:
        if len(handlandmarks) != 0:
            while handlandmarks[4][3] == "Right":
                if handlandmarks[4][1] > handlandmarks[3][1]:
                    cv2.putText(img, str("Right thumb up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                elif handlandmarks[8][2] < handlandmarks[6][2]:
                    cv2.putText(img, str("Right index up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                elif handlandmarks[12][2] < handlandmarks[10][2]:
                    cv2.putText(img, str("Right Middle finger up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                (255, 0, 0), 2)
                elif handlandmarks[16][2] < handlandmarks[14][2]:
                    cv2.putText(img, str("Right ring finger up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),
                                2)
                elif handlandmarks[20][2] < handlandmarks[18][2]:
                    cv2.putText(img, str("Right pinky up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                break

            while handlandmarks[4][3] == "Left":
                if handlandmarks[4][1] < handlandmarks[3][1]:
                    cv2.putText(img, str("Left thumb up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                elif handlandmarks[8][2] < handlandmarks[6][2]:
                    cv2.putText(img, str("Left index up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                elif handlandmarks[12][2] < handlandmarks[10][2]:
                    cv2.putText(img, str("Left Middle finger up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),
                                2)
                elif handlandmarks[16][2] < handlandmarks[14][2]:
                    cv2.putText(img, str("Left ring finger up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),
                                2)
                elif handlandmarks[20][2] < handlandmarks[18][2]:
                    cv2.putText(img, str("Left pinky up"), (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                break

    cv2.imshow("Test", img)
    cv2.waitKey(1)

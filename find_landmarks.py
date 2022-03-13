import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


class HandDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(max_num_hands=2,
                                    min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5)

    def find_landmarks(self, image, handnumber=0, draw=False):
        originalimg = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)
        landmarks = []

        if results.multi_handedness:
            label = results.multi_handedness[handnumber].classification[0].label
            if label == "Left":
                label = "Right"
            elif label == "Right":
                label = "Left"

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[handnumber]

            for imgid, landmark in enumerate(hand.landmark):
                imgheight, imgwidth, imgcenter = originalimg.shape
                x, y = int(landmark.x * imgwidth), int(landmark.y * imgheight)
                landmarks.append([imgid, x, y, label])

            if draw:
                mp_drawing.draw_landmarks(originalimg, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style())
        return landmarks

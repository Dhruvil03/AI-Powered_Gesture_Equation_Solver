import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
import os
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
st.image('images.jpg')

col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.subheader("")

genai.configure(api_key="AIzaSyDSas_AQfvD0ntckyv4KoXFHen_NWdQtfE")
model = genai.GenerativeModel("gemini-1.5-flash")

cap = cv2.VideoCapture(0)
cap.set(propId=3, value=1280)
cap.set(propId=4, value=720)
# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHand(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers, lmList
    else:
        return None

def draw(info,prev_pos,canvas):
    fingers, lmList = info
    current_pos= None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None: prev_pos = current_pos
        cv2.line(canvas,current_pos,prev_pos,(255,0,255),10)
    elif fingers == [1, 1, 1, 1, 1]:
        canvas = np.zeros_like(img)
    # return current_pos, canvas

def sentToAI(model, canvas, fingers):
    if fingers == [1,1,1,1,0]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve this Math Problem", pil_image])
        # response = model.generate_content("Which is the largest ocean?")
        return response.text


prev_pos = None
canvas = None
img_combined = None
ans = ""
while True:
    success, img = cap.read()
    # flip the image
    img = cv2.flip(img, flipCode=1)
    if canvas is None:
        canvas = np.zeros_like(img)

    info = getHand(img)
    if info:
        fingers, lmlist = info
        prev_pos = draw(info, prev_pos, canvas)
        ans = sentToAI(model, canvas, fingers)
        # Assuming img and canvas are already loaded and are of the same size and type
    img_combined = cv2.addWeighted(img, 0.85, canvas, 0.15, 0)
    FRAME_WINDOW.image(img_combined, channels="BGR")
    if ans:
        output_text_area.text(ans)
    # Display the image in a window
    # cv2.imshow("Image", img)
    # cv2.imshow("Canvas", canvas)
    # cv2.imshow("Img_combines", img_combined)
    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)





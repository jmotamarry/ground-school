import cv2
import numpy as np

input_video = '../videos/Minecraft_stitch_test.mp4'
output_image = '../images/stitched.png'
cap = cv2.VideoCapture(input_video)
frames = []

print("Reading frames from video.")

i = 0
while True:
    ret, frame = cap.read()     # read next frame
    if not ret:
        break
    
    if i % 20 == 0:
        frames.append(frame)
    
    i += 1

cap.release()
print(len(frames))

print("Stitching frames.")
stitcher = cv2.Stitcher_create(cv2.STITCHER_SCANS)
status, panorama = stitcher.stitch(frames)

if status == cv2.Stitcher_OK:
    print("Saving image.")
    cv2.imwrite(output_image, panorama)
else:
    print("Error during stitching.")
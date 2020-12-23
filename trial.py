import cv2
cap = cv2.VideoCapture("C:/Users/15216/Desktop/script_in_docker/video_origin/55.mp4")
num = cap.get(7)
print(num)
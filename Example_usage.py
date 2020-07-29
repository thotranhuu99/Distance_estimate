from Distance_functions import distance_estimate
import cv2
import sys

def nothing(x):
    pass


img = cv2.imread("0_ball_1256.jpg")
cv2.namedWindow('Window 1')
cv2.createTrackbar('Var_1', 'Window 1', 300, 1000, nothing)
cv2.createTrackbar('Var_2', 'Window 1', 900, 1000, nothing)
#print(distance)
test = True
while 1:
    Min_val = cv2.getTrackbarPos('Var_1', 'Window 1')
    Max_val = cv2.getTrackbarPos('Var_2', 'Window 1')
    distance, img_1, error = distance_estimate(img, [257, 12], [397, 208], 0.2, Min_val, Max_val, 7)
    if error == 0:
        cv2.imshow('Window 1', img_1)
        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break
    else:
    # print(distance)
        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break

from Distance_functions import distance_estimate
import cv2


def nothing(x):
    pass


img = cv2.imread("2_clamp_1177.jpg")
cv2.namedWindow('Window 1')
cv2.createTrackbar('Var_1', 'Window 1', 462, 1000, nothing)
cv2.createTrackbar('Var_2', 'Window 1', 974, 1000, nothing)
#print(distance)
while 1:
    distance, img_1 = distance_estimate(img, [257, 12], [397, 208], 0.2, cv2.getTrackbarPos('Var_1', 'Window 1'),
                                        cv2.getTrackbarPos('Var_2', 'Window 1'))
    cv2.imshow('Window 1', img_1)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

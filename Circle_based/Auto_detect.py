import numpy as np
import argparse
import cv2
import time


def nothing():
    pass


# Example usage: python3 Detect_circle.py --image ./Changed_data/20.jpg
# For Pycharm: Edit Configuration -> Parameters -> --image ./Changed_data/20.jpg
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.namedWindow('Window 1')
Canny_low = 300
Canny_high = 500
Canny_step = 1
Canny_param = Canny_high
while True:
    start_time = time.time()
    output = img.copy()
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=Canny_param, param2=22, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        cv2.imshow("Window 1", np.hstack([img, output]))
        if len(circles) is not 1:
            if Canny_param < Canny_high:
                Canny_param += Canny_step
        else:
            pass
    else:
        if Canny_param >= Canny_low + Canny_step:
            Canny_param -= Canny_step
        else:
            pass
        cv2.imshow("Window 1", np.hstack([img, img]))
    print(Canny_param)
    stop_time = time.time()
    print("{}".format(stop_time-start_time))
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

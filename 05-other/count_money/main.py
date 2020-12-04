import cv2
import numpy as np


def find_money_value(circumferences):
    value = 0
    for i in range(len(circumferences)):
        if circumferences[i] > 60:
            value += 1
        elif circumferences[i] > 50:
            value += 0.5
        elif circumferences[i] > 48 and circumferences[i]<= 50:
            value += 0.25
        elif circumferences[i] > 40 and circumferences[i] <= 48:
            value += 0.10
        else:
            value += 0.05

    return value







img = cv2.imread('2.jpg', 0)
img = cv2.medianBlur(img,5)
#blurred = cv2.GaussianBlur(img, (17, 17), 20)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

cv2.imshow("First window",cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


circles = circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50,param1=150, param2=60,minRadius = 20, maxRadius = 100)


circles = np.uint16(np.around(circles))

circumferences = []

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # cv2.circle(img, center, radius, color, thickness=1, lineType=8, shift=0)

    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.putText(cimg, ("circumference: " + str(i[2])), (int(i[0] - 30),int(i[1] - 30)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0,0), 2)

    circumferences.append(i[2])



circumferences.sort(reverse=True)
print(circumferences)

miktar = find_money_value(circumferences)
print(miktar , " lira")



cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

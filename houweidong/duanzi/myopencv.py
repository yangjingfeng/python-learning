import cv2

# img = cv2.imread('scenery.jpeg')
# cv2.namedWindow("Image")
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

img = cv2.imread("welcome.gif")
cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("image", img)
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
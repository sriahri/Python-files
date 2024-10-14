# Import opencv
import cv2

# Manipulating the image
# Load the input image
img = cv2.imread('input.jpg')

# Obtain the dimensions
(row, col) = img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Reconstructing the image to its originality
(row, col) = img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) / 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

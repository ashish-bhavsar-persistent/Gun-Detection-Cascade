import cv2


def resize():
    img = cv2.imread("C:/Users/ashishkumar_bhavsar/Downloads/armas2.png", cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(img, (50, 50))
    cv2.imwrite('arms2.png', resized_image)


resize()
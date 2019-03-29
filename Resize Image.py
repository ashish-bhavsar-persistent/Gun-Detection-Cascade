import cv2
import os

def resize():

        # for file_type in ['neg']:
        #     for img in os.listdir(file_type):
        #         current_image_path = str(file_type) + "/" + str(img)
        #         img1 = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
        #         resized_image = cv2.resize(img1, (630, 360))
        #         cv2.imwrite(current_image_path, resized_image)

        current_image_path = "gun.jpg"
        img1 = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img1, (315, 180))
        cv2.imwrite(current_image_path, resized_image)

resize()
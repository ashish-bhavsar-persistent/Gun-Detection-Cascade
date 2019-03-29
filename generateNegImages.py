import os
import cv2


def generate():

    count = 1000
    for file_type in ['Raw']:
        for img in os.listdir(file_type):
            for i in  range (400):
                current_image_path = str(file_type) + "/" + str(img)
                img1 = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img1, (100, 100))
                cv2.imwrite('neg/'+str(count)+".jpg", resized_image)
                count+=1


generate()
import cv2
import numpy as np

if __name__ == "__main__":
    # image = cv2.imread('Y:/지어소프트_전달데이터/200602_front/20200602_133422/20200602_133422/1_20200602_133422/img/00000.jpg')

    ff = np.fromfile('Y:/지어소프트_전달데이터/200602_front/20200602_133422/20200602_133422/1_20200602_133422/img/00000.jpg', np.uint8)
    image = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) 
    print(np.shape(image))
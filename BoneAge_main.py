import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

#Opening images in folder
#training_paths = pathlib.Path('dataset').glob('*/images/*.png')
DATA_DIRECTION="dataset"
CATEGORIES =['LeftBone']
WIDTH=500
HEIGHT = 600
#filenames = os.listdir("dataset/")
#features = os.listdir("Features/Middle Finger")
#dosyaİsmi = "Features/Middle Finger/ROI_sampleimage.jpg"

training_data=[]

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA_DIRECTION, category)
        class_num=CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(WIDTH,HEIGHT))
                plt.imshow(new_array,cmap="gray")
                plt.title('Hand Wrist Images:')
                edges = cv2.Canny(new_array,15,30)
                plt.subplot(121),plt.imshow(new_array,cmap = 'gray')
                plt.title('Original Image'), plt.xticks([]), plt.yticks([])
                plt.subplot(122),plt.imshow(edges,cmap = 'gray')
                plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
                plt.show()
                #region = edges[90:455, 180:240]
                #cv2.imshow('Selected images with ROI', region)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                # Erotion & Dilation
                # kernel = np.ones((5,5), np.uint8)
                # erosion = cv2.erode(img_array, kernel, iterations=1)
                # dilation = cv2.dilate(img_array, kernel, iterations=1)
                # plt.subplot(321), plt.imshow(img_array), plt.title('Original Image')
                # plt.xticks([]), plt.yticks([])
                # plt.subplot(322), plt.imshow(erosion), plt.title('Erosioned Image')
                # plt.xticks([]), plt.yticks([])
                # plt.subplot(323), plt.imshow(dilation), plt.title('Dilated Image')
                # plt.xticks([]), plt.yticks([])

                training_data.append([new_array,class_num])

            except Exception as e:
                pass
create_training_data()
#Image Preprocessing: erosion & dilation


#Image Segmentation

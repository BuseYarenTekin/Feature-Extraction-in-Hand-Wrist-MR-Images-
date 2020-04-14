import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

DATA_DIRECTION="data_preprocess"
CATEGORIES =['Left']
#WIDTH=500
#HEIGHT =500
training_data=[]

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA_DIRECTION, category)
        class_num=CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                #new_array = cv2.resize(img_array,(WIDTH,HEIGHT))
                imagenumpyarray=np.array(img_array)
                #imagelist=np.ndarray.tolist(imagenumpyarray)
                asaray=np.asarray(imagenumpyarray)
                #print("Np array: ",imagenumpyarray)
                print("List:",asaray)
                plt.imshow(img_array,cmap="gray")
                plt.title("El bilek")
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                training_data.append([img_array, class_num])
            except Exception as e:
                pass

create_training_data()
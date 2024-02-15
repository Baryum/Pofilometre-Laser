from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from Sample import *


CAM_FOLDER = "./images/"


def fetchImages(folder = CAM_FOLDER):
    imgList = []
    for i in os.listdir(folder):
        imageName = "img" + str(Sample.nextId) + ".png" 
        image = Sample(path=imageName, ogPxValues=np.asarray(Image.open(folder + i)))
        imgList.append(image)
        #imgList.append()
    return imgList


if __name__ == "__main__":
    print(fetchImages()[0].ogPxValues)
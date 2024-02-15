from PIL import Image
import pandas as pd
import numpy as np
import Sample

def laserIsolation(s, lb, ub):
    filteredPxValues = np.array(s.ogPxValues)
    #filteredPxValues = np.clip((filteredPxValues - lb) * (255 / (ub - lb)), 0, 255).astype(np.uint8)
    print(filteredPxValues)
    for x in range(len(filteredPxValues)):
        for y in range(len(filteredPxValues[1])):
            for c in range(3):
                if filteredPxValues[x][y][c] - lb >= 0:
                    filteredPxValues[x][y][c] -=  lb
                else:
                    filteredPxValues[x][y][c] = 0
                if filteredPxValues[x][y][c] * 255 / (ub - lb) <= 255:
                    filteredPxValues[x][y][c] *= 255 / (ub - lb)
                else:
                    filteredPxValues[x][y][c] = 255

    s.filteredPxValues = filteredPxValues
    return s

def createSample(path):
    sample = Sample.Sample("images/test.png")
    return sample

def getImage(sample):
    pxValues = sample.filteredPxValues
    pxValues = np.reshape(pxValues, sample.shape)
    img = Image.fromarray(pxValues)

    img.save('output.png')

    img.show()

if __name__ == "__main__":
    s = createSample("image de test")
    s = laserIsolation(s, 150, 200)
    getImage(s)


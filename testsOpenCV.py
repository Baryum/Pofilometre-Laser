import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

img = cv.imread('images/lowrestest1.png')

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#essai de lecture par boucles
height, width = imgGray.shape
tab = []
tab = [0, 0, 0, 0, 2, 8, 17, 34, 58, 94, 135, 177, 213, 245, 255, 248, 220, 183, 141, 102, 65, 39, 17, 8, 0, 0, 0, 0, 0]    #valeurs de test

def gaussian(x, μ, sig):
    return (1 / (sig * np.sqrt(2 * np.pi))) * np.exp(-((x - μ) ** 2) / (2 * sig** 2))


print("imggray : ", imgGray.shape)
for x in range(width):
    """for y in range(height):
        tab.append(imgGray[y, x])"""

    print(tab)
    xdata = np.linspace(0, len(tab)-1, num=len(tab))
    xdatagrand = np.linspace(0, len(tab)-1, num=len(tab)*10)
    popt, pcov = curve_fit(gaussian, xdata=xdata, ydata=tab)
    print("res = ", popt)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(xdata, tab, 'ro')
    ax2.plot(xdatagrand, gaussian(xdatagrand, popt[0], popt[1]), '-r')
    
    plt.show()
    break #on arrête à la première itération c bon là oh
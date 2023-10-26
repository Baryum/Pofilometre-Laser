from fetchImages import *
from Sample import *
if __name__ == "__main__":
    imagesList = fetchImages()

    img1 = Sample("img1", imagesList)
    img2 = Sample("img2", None)

    print(img1, img2)
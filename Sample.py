from PIL import Image
import numpy as np

class  Sample():
    nextId = 0

    def __init__(self, path):
        self.id = Sample.nextId
        Sample.nextId += 1
        
        im = Image.open(path)
        self.name = path
        self.ogPxValues = np.asarray(im)
        self.shape = self.ogPxValues.shape
        self.filteredPxValues = np.zeros(self.shape)

    def getImage(self, pxValues):
        img = Image.fromarray(self.nvPxValues)

        img.save('output.png')

        img.show()

        
    def __str__(self) -> str:
        return f"Sample {self.id} : \nname={self.name}\nogPxValues={self.ogPxValues is not None}\nfilteredPxValues={self.filteredPxValues is not None}"
    
    def __repr__(self) -> str:
        pass

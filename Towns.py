import random, os
from PIL import Image



class Town:
    def __init__(self, w, h):
        self.LandWidth, self.LandHeight = w, h

    def CreateImage(self):
        with Image.new("RGB", (self.LandWidth, self.LandHeight), (66,245,120)) as Img:
            ImagePixels = Img.load()
            # TODO: Add code for saving town layout to an image

            Img.show()
            Img.close()

    def Generate(self):
        pass



t = Town(100, 100)
t.CreateImage()
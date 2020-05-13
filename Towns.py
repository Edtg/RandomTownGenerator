import random, os
from PIL import Image



class Town:
    def __init__(self, w, h, Entrances, Branches, Density):
        self.LandWidth = w
        self.LandHeight = h
        self.Entrances = Entrances
        self.Branches = Branches
        self.Density = Density

    def CreateImage(self):
        with Image.new("RGB", (self.LandWidth, self.LandHeight), (66,245,120)) as Img:
            ImagePixels = Img.load()
            # TODO: Add code for saving town layout to an image

            Img.show()
            Img.close()

    def Generate(self):
        pass




class Road:
    def __init__(self, StartPos, EndPos, w):
        self.Start = Start
        self.End = End
        self.width = w


class MainRoad(Road):
    def __init__(self, StartPos, EndPos, w):
        super(StartPos, EndPos, w)

class SubRoad(Road):
    def __init__(self, StartPos, EndPos, w):
        super(StartPos, EndPos, w)


t = Town(250, 200, 2, 10, 3)
t.CreateImage()
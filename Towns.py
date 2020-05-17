import random, os, math
from PIL import Image
from scipy import interpolate



Clamp = lambda Value, MinValue, MaxValue: max(min(Value, MaxValue), MinValue)

CurveEquation = lambda X, P, Q, E: round(((P + Q - (2*E)) * pow(X, 3)) + (((3*E) - (2*P) - Q) * pow(X, 2)) + (P * X))

Diff = lambda A, B: abs(A - B)

Grad = lambda X1, Y1, X2, Y2: (Y2 - Y1) / (X2 - X1)


class Town:
    def __init__(self, w, h, Branches, Density, Spread):
        self.LandWidth = w
        self.LandHeight = h
        self.Branches = Branches
        self.Density = Density
        self.Spread = Spread
        self.Roads = [MainRoad([], 4)]

    def CreateImage(self):
        with Image.new("RGB", (self.LandWidth, self.LandHeight), (66,245,120)) as Img:
            ImagePixels = Img.load()
            # TODO: Add code for saving town layout to an image

            # Get Roads
            for r in self.Roads:
                RoadLine = interpolate.splrep([a.x for a in r.Vertices], [b.y for b in r.Vertices])
                for X in range(self.LandWidth):
                    for Y in range(self.LandHeight):
                        if Y == math.floor(interpolate.splev(X, RoadLine)):
                            ImagePixels[X, Y] = (0,0,0)





            Img.show()
            Img.close()

    def Generate(self):
        # Generate main road
        Highest = self.LandHeight/4
        Lowest = self.LandHeight*(3/4)

        LeftEntry = RoadVertex(0, random.randint(Highest, Lowest))
        NumVertices = 4
        DesiredDistance = 25
        NumVertices = math.floor(self.LandWidth/DesiredDistance)

        Curve = 5

        self.Roads[0].AddVertexEnd(LeftEntry)
        for v in range(1, NumVertices):
            self.Roads[0].AddVertexEnd(RoadVertex(v * DesiredDistance, Clamp(self.Roads[0].GetEndVertex().y + random.randint(-Curve, Curve), Highest, Lowest)))
        RightEntry = RoadVertex(self.LandWidth-1, self.Roads[0].GetEndVertex().y + random.randint(-Curve, Curve))
        self.Roads[0].AddVertexEnd(RightEntry)

        


        


    def GetRandomPointOnSide(self, Side):
        if Side == 1 or Side == 2: # Left/Right
            y = random.randint(0, self.LandHeight)
            x = 0 if Side == 1 else self.LandWidth
        else: # Top/Bottom
            x = random.randint(0, self.LandWidth)
            y = 0 if Side == 3 else self.LandHeight

        return (x, y)

            


class RoadVertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Road(object):
    def __init__(self, Vertices, w):
        self.Vertices = Vertices
        self.width = w
    
    def AddVertexEnd(self, Vertex):
        self.Vertices.append(Vertex)

    def AddVertexMid(self, NewVertex, AfterVertex):
        Lhs = self.Vertices[:self.Vertices.index(AfterVertex)]
        Rhs = self.Vertices[self.Vertices.index(AfterVertex):]
        self.Vertices = Lhs + NewVertex + Rhs

    def AddVertexMidI(self, NewVertex, AfterIndex):
        Lhs = self.Vertices[:AfterIndex]
        Rhs = self.Vertices[AfterIndex:]
        self.Vertices = Lhs + NewVertex + Rhs

    def GetEndVertex(self):
        return self.Vertices[len(self.Vertices)-1]
    
    def GetNextVertex(self, Vertex):
        return self.Vertices[self.Vertices.index(Vertex)+1]


class MainRoad(Road):
    def __init__(self, Vertices, w):
        super().__init__(Vertices, w)

class SubRoad(Road):
    def __init__(self, Vertices, w):
        super().__init__(Vertices, w)


t = Town(250, 200, 10, 3)
t.Generate()
t.CreateImage()
#Assignment 14

''' Parent Class Box '''
class Box:
    def getVolume(self):
        vol = self.length * self.breadth * self.height
        return vol
    def __init__(self,length,breadth,height):
        self.length = length
        self.height = height
        self.breadth = breadth

''' Child Class BigBox '''
class BigBox(Box):
    def __init__(self,length,breadth,height):
        Box.__init__(self,length,breadth,height)
    def getCapacity(self,sBox):
        bigvol = self.getVolume()
        smallvol = sBox.getVolume()
        return int(bigvol/smallvol)
        
smallBox = Box(1,1,1)
bigBox = BigBox(4,4,4)
capacity = bigBox.getCapacity(smallBox)
print("Number of small boxes in large one are:",capacity)

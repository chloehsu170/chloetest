#coding = utf-8

class Widget:
    def __init__(self,size =(50,50)):
        self._size = size
    def getSize(self):
        return self._size
    def setSize(self,width,length):
        if width < 0 or length < 0:
            raise ValueError, "wrong size"
        self._size =(width,length)
    def dispose(self):
        pass
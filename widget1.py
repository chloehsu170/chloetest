class Widget1:
    def __init__(self,size=(10,10)):
        self._size = size
    def getSize(self):
        return self._size
    def setSize(self,width,length):
        if width < 0 or length < 0:
            raise ValueError, "WRONG SIZE"
        self._size = (width,length)
    def dispose(self):
        pass
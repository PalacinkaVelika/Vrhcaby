from Piece import Piece

class Field():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._content = [] #stores Pieces
        
        
        
    @property
    def content(self): #getter
        return self._content  
    @property
    def x(self): #getter
        return self._x
    @x.setter
    def x(self, value): #setter
        self._x = value
    @property
    def y(self): #getter
        return self._y
    @y.setter
    def y(self, value): #setter
        self._y = value
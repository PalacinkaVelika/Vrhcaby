
class Player():
    def __init__(self, id, name, symbol):
        self._id = id
        self._name = name
        self._symbol = symbol
        self._wins = 0
        
        
    @property
    def symbol(self): #getter
        return self._symbol    
    @property
    def id(self): #getter
        return self._id  
    @property
    def name(self): #getter
        return self._name
    @name.setter
    def name(self, value): #setter
        self._name = value
    @property
    def wins(self): #getter
        return self._wins
    @wins.setter
    def wins(self, value): #setter
        self._wins = value
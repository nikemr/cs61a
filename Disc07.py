from doctest import testmod

class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size=0
    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size+=1


    def pop(self):
        """ Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        self.size-=1
        return self.items.pop(self.items.index(min(self.items)))
        


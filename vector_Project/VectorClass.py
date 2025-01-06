import math

class Vector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def magnitude(self):

        return math.sqrt(self.x**2 + self.y**2)
    
    def __add__(self, other):

        return Vector(self.x + other.x, self.y + other.y)
    
    def __lt__(self, other):

        return self.magnitude() < other.magnitude()
    
    def __str__(self):
        if self.y >= 0:
            return f'{self.x}x + {self.y}y'
        else:
            return f'{self.x}x - {-self.y}y'
        
    def __eq__(self, other):

        return self.x == other.x and self.y == other.y
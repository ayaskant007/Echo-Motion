class Vector:
    def __init__(self):
        self.x, self.y, self.x = 1

    def __add__(self, other):
        result  = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __str__(self):
        return f"Vector({self.x,}, {self.y}, {self.z})"
    
    def __len__(self):
        return 3
    
v1 = Vector([1,2,3])
print(len(v1))
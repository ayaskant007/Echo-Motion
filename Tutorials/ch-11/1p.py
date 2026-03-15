class TwoVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector of 2D is {self.i}i, {self.j}j")

class ThreeVector(TwoVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The vector of 3D is {self.i}i, {self.j}j and {self.k}k.")


a = TwoVector(1, 2)
a.show()
b = ThreeVector(1,2,3)
b.show()
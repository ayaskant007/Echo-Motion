from functools import reduce

l = [1,2,3,4,5]

square = lambda x: x*x

sqList = map(square, l)

print(list(sqList))

#  Filter

def even(n):
    if (n%2 == 0):
        return True
    else:
        return False
    
onlyEven = filter(even, l)
print(list(onlyEven))

#  Reduce
def sum(a,b):
    return a+b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))
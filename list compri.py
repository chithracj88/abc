# list1=(i for i in range (21) if i%2==0)
# print(list1)

class NewClass:

    def __init__(self,max=0):
        self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2** self.n
            self.n +=1
            return result
        else:
            raise stopiteration
numbers= NewClass(3)

i=iter(numbers)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
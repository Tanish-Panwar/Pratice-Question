# 1. Create a class C-2d vector and use it to create another class representing a 3-d vecor
class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return     f"{self.icap}i + {self.jcap}j"

class C3dVec:
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"    

v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)






# 2. Create a class pets from a class animals and further create class Dog from pets add a method beak to class Dog
class Animlas:
    animal = "dog"

class Pets:
    color = "brown"

class Dog:
    @staticmethod
    def bark():
        print("barking")


d = Dog()
d.bark()








# 3. Create a class Employee and add salary and increment properties to it.
# write a method salaryAfterIncreent method with a @property decorator with a setter which changes the value of increment based on the salary
# salarAfterIncrement = salary * increment
class Employee:
    salary = 200
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self/salary

e = Employee()
print(e.salaryAfterIncrement)










# 4. Write a class complex to represent a vector of n dimension. overload operator + and * which adds and multiplies them
# Formula to calculate Complex Num:- (a+bi)=(ac-bd)+(ad+bc)i
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imagin = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imagin + c.imagin)    

    def __mul__(self, c):
        mulReal = self.real*c.real-self.imagin*c.imagin
        mulImg = self.real*c.imagin+self.imagin*c.real
        return Complex(mulReal, mulImg)     

    def __str__(self):
        return f"{self.real}r {self.imagin}i"



c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(c1 *c2)










# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot product of them
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index}"
            index +=1
        return str1    

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum =  0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum   

# 7. Override a len method in 5thQ to display dimensions of vector 
    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
# print(v1 + v2)
# print(v1 * v2)
print("dimensions", len(v2))
print("dimensions", len(v1))











# 6. Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# assume Vector of dimensions 3 for this problem

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i  + {self.vec[1]}j  + {self.vec[2]}k "  


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)
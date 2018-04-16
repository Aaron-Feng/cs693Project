import sys

class CohesionExample1:
    # This is a class with LCOM4 = 2

    def __init__(self):
        self.x = 2
        self.y = 3

    def a(self):
        self.b()
        return

    def b(self):
        temp = self.x + 2
        return temp

    def c(self):
        res = self.y / 2
        return res

    def d(self):
        result = self.y * 2
        self.e()
        return result

    def e(self):
        pass

class CohesionExample2:
    # This is a class with LCOM4 = 1

    def __init__(self):
        self.x = 1
        self.y = 2

    def a(self):
        self.b()
        return

    def b(self):
        temp = self.x + 2
        return temp

    def c(self):
        res = self.y / 2
        res = res + self.x
        return res

    def d(self):
        result = self.y * 2
        self.e()
        return result

    """ this method does nothing """
    def e(self):
        pass

class CouplingExample1:

    def __init__(self):
        self.otherClass = CouplingExample2()
        pass

    def n1(self):
        self.otherClass.m1()
        a=CouplingExample2.m2()
        b=CohesionExample2.a()

class CouplingExample2:

    def __init__(self):
        pass

    def m1(self):
        pass

    def m2(self):
        pass
class DepthOfInheritanceExample1(object):
    def c(self):
        pass
    def __init__(self):
        pass

class DepthOfInheritanceExample2(DepthOfInheritanceExample1):
    class inner:
        def __init__(self):
            pass

    def __init__(self):
        pass

class DepthOfInheritanceExample3(DepthOfInheritanceExample2):

    def __init__(self):
        pass

class DepthOfInheritanceExample4(DepthOfInheritanceExample3):

    def __init__(self):
        pass

class NumberOfChildrenExample1:

    def __init__(self):
        pass

class NumberOfChildrenExample2(NumberOfChildrenExample1):

    def __init__(self):
        pass

class NumberOfChildrenExample3(NumberOfChildrenExample1):

    def __init__(self):
        pass

"""
The output of your program should be something similar as following with the (mostly) default parameters of the metrics. Only DIT's object parameter is set to ON.

>>>> OUTPUT START

LOC (comments=OFF,emptyLines=OFF,imports=ON)
---
72


LCOM4
-----
CohesionExample1 = 2
CohesionExample2 = 1
CouplingExample1 = 1
CouplingExample2 = 0
DepthOfInheritanceExample1 = 0
DepthOfInheritanceExample2 = 0
DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample4 = 0
NumberOfChildrenExample1 = 0
NumberOfChildrenExample2 = 0
NumberOfChildrenExample3 = 0


CBO
---
CohesionExample1 <-> CohesionExample2 = 0
CohesionExample1 <-> CouplingExample1 = 0
CohesionExample1 <-> CouplingExample2 = 0
CohesionExample1 <-> DepthOfInheritanceExample1 = 0
CohesionExample1 <-> DepthOfInheritanceExample2 = 0
CohesionExample1 <-> DepthOfInheritanceExample3 = 0
CohesionExample1 <-> DepthOfInheritanceExample4 = 0
CohesionExample1 <-> NumberOfChildrenExample1 = 0
CohesionExample1 <-> NumberOfChildrenExample2 = 0
CohesionExample1 <-> NumberOfChildrenExample3 = 0
CohesionExample2 <-> CouplingExample1 = 0
CohesionExample2 <-> CouplingExample2 = 0
CohesionExample2 <-> DepthOfInheritanceExample1 = 0
CohesionExample2 <-> DepthOfInheritanceExample2 = 0
CohesionExample2 <-> DepthOfInheritanceExample3 = 0
CohesionExample2 <-> DepthOfInheritanceExample4 = 0
CohesionExample2 <-> NumberOfChildrenExample1 = 0
CohesionExample2 <-> NumberOfChildrenExample2 = 0
CohesionExample2 <-> NumberOfChildrenExample3 = 0
CouplingExample1 <-> CouplingExample2 = 1
CouplingExample1 <-> DepthOfInheritanceExample1 = 0
CouplingExample1 <-> DepthOfInheritanceExample2 = 0
CouplingExample1 <-> DepthOfInheritanceExample3 = 0
CouplingExample1 <-> DepthOfInheritanceExample4 = 0
CouplingExample1 <-> NumberOfChildrenExample1 = 0
CouplingExample1 <-> NumberOfChildrenExample2 = 0
CouplingExample1 <-> NumberOfChildrenExample3 = 0
CouplingExample2 <-> DepthOfInheritanceExample1 = 0
CouplingExample2 <-> DepthOfInheritanceExample2 = 0
CouplingExample2 <-> DepthOfInheritanceExample3 = 0
CouplingExample2 <-> DepthOfInheritanceExample4 = 0
DepthOfInheritanceExample1 <-> DepthOfInheritanceExample2 = 0
DepthOfInheritanceExample1 <-> DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample1 <-> DepthOfInheritanceExample4 = 0
DepthOfInheritanceExample1 <-> NumberOfChildrenExample1 = 0
DepthOfInheritanceExample1 <-> NumberOfChildrenExample2 = 0
DepthOfInheritanceExample1 <-> NumberOfChildrenExample3 = 0
DepthOfInheritanceExample2 <-> DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample2 <-> DepthOfInheritanceExample4 = 0
DepthOfInheritanceExample2 <-> NumberOfChildrenExample1 = 0
DepthOfInheritanceExample2 <-> NumberOfChildrenExample2 = 0
DepthOfInheritanceExample2 <-> NumberOfChildrenExample3 = 0
DepthOfInheritanceExample3 <-> DepthOfInheritanceExample4 = 0
DepthOfInheritanceExample3 <-> NumberOfChildrenExample1 = 0
DepthOfInheritanceExample3 <-> NumberOfChildrenExample2 = 0
DepthOfInheritanceExample3 <-> NumberOfChildrenExample3 = 0
DepthOfInheritanceExample4 <-> NumberOfChildrenExample1 = 0
DepthOfInheritanceExample4 <-> NumberOfChildrenExample2 = 0
DepthOfInheritanceExample4 <-> NumberOfChildrenExample3 = 0
NumberOfChildrenExample1 <-> NumberOfChildrenExample2 = 0
NumberOfChildrenExample1 <-> NumberOfChildrenExample3 = 0
NumberOfChildrenExample2 <-> NumberOfChildrenExample3 = 0


DIT (object=ON)
---
CohesionExample1 = 0
CohesionExample2 = 0
CouplingExample1 = 0
CouplingExample2 = 0
DepthOfInheritanceExample1 = 1
DepthOfInheritanceExample2 = 2
DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample4 = 1
NumberOfChildrenExample1 = 0
NumberOfChildrenExample2 = 1
NumberOfChildrenExample3 = 1


NOC
---
CohesionExample1 = 0
CohesionExample2 = 0
CouplingExample1 = 0
CouplingExample2 = 0
DepthOfInheritanceExample1 = 0
DepthOfInheritanceExample2 = 0
DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample4 = 0
NumberOfChildrenExample1 = 2
NumberOfChildrenExample2 = 0
NumberOfChildrenExample3 = 0


WMC (constructor=OFF)
---
CohesionExample1 = 5
CohesionExample2 = 5
CouplingExample1 = 1
CouplingExample2 = 1
DepthOfInheritanceExample1 = 0
DepthOfInheritanceExample2 = 0
DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample4 = 0
NumberOfChildrenExample1 = 0
NumberOfChildrenExample2 = 0
NumberOfChildrenExample3 = 0

>>>> OUTPUT END


Some different outputs w.r.t. the parameters are below. Not all items are displayed but just the different ones. Your report should show ALL.

>>>> OUTPUT START

LOC (comments=ON,emptyLines=ON,imports=OFF)
---
278


DIT (object=OFF)
---
CohesionExample1 = 0
CohesionExample2 = 0
CouplingExample1 = 0
CouplingExample2 = 0
DepthOfInheritanceExample1 = 0
DepthOfInheritanceExample2 = 1
DepthOfInheritanceExample3 = 0
DepthOfInheritanceExample4 = 1
NumberOfChildrenExample1 = 0
NumberOfChildrenExample2 = 1
NumberOfChildrenExample3 = 1


WMC (constructor=ON)
---
CohesionExample1 = 6
CohesionExample2 = 6
CouplingExample1 = 2
CouplingExample2 = 2
DepthOfInheritanceExample1 = 1
DepthOfInheritanceExample2 = 1
DepthOfInheritanceExample3 = 1
DepthOfInheritanceExample4 = 1
NumberOfChildrenExample1 = 1
NumberOfChildrenExample2 = 1
NumberOfChildrenExample3 = 1

>>>> OUTPUT END

"""
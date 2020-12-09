class school:
    _a = 1
    _b = 2
    _c = 3
    _d = 4
    list = [ ]

    def rekenen(self):
        print("A kan je zien als een nummer")
        print("er zijn 26 letters in de alfabet")
    def func2(self):
        print(school._b, "is getal 2")

class leerling(school):
    school._a += 1
    school._b += 1
    school.list.append("a")
    _e = 5
    _f = 6
    def func(self):
        super().func2()
        _g = 7
        _h = 8
        print("test")
    
    
class1 = school()
class2 = leerling()

class1.rekenen()
class2.func()

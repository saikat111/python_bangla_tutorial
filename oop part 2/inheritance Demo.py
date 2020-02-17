class X:
    name ="Saikat"
    def n(self):
        print(self.name)

class Y(X):
    name2 = "RAKIB"
    def nn(self):
        print(self.name2)

y = Y()
y.n()
y.nn()
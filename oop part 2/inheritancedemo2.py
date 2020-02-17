class A:
    def __init__(self,num1):
        self.num1 = num1

    def num(self):
        print(self.num1)

class B(A):
    def __init__(self,num1,num2):
        A.__init__(self,num1)
        self.n = num2

    def run(self):
        print(self.num1,self.n)
        print("__________")
        self.num()


class X(B):
    def __init__(self,num1,n,name):
        B.__init__(self,num1,n)
        self.nn = name

    def rr(self):
        print(self.num1,self.n,self.nn)
        print("_________")
        self.run()
        print("_________")
        self.num()
        print("_________")


x = X(40,60,"saikat")
x.rr()
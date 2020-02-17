class A:
    def __init__(self,num1 ,num2):
        self.num1 = num1
        self.num2 = num2

    def p(self):
        print(self.num1 + self.num2)


class B:
    def __init__(self,name1 ,nmae2):
        self.name1= name1
        self.nmae2 = nmae2

    def p(self):
        print(self.nmae2 ,self.name1)

a = A(50,100)
a.p()
b = B("saikat", "Rakib")
b.p()

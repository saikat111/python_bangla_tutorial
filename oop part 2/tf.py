class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self,fname,lname, f, l):
    Person.__init__(self, fname, lname)
      self.f= f
      self.l =l

x = Student("Mike", "Olsen","a","a")
x.printname()
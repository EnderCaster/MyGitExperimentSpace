#!/usr/bin/env python3
# -*- utf-8 -*-
# and a class can extends more than one class
# dont use getters and setters in python
class Person(object):
    """person is a base class
    """
    def __init__(self,name):
        self.name=name
    def get_details(self):
        return self.name
class Student(Person):
    """extends Person
    """
    def __init__(self,name,branch,year):
        """use var self as usual, nothing special
        """
        Person.__init__(self,name)
        self.branch=branch
        self.year=year
    def get_details(self):
        return "{} studies {} and is in {} year".format(self.name,self.branch,self.year)
class Teacher(Person):
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers=papers
    def get_details(self):
        return "{} teaches {}".format(self.name,",".join(self.papers))

person=Person("Sachin")
student=Student("Kushal","CSE",2005)
teacher=Teacher("Prashad",["c","C-fuck"])

print(person.get_details())
print(student.get_details())
print(teacher.get_details())
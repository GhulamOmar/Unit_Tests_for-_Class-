"""
Program: student_class.py
Author: Ghulam Omar
Last date modified: 10/29/2019
This is an example of student class contains a diver and unit test
"""


class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        last_name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not (major_characters.issuperset(major) and major_characters.issuperset(major)):
            raise ValueError
        if not (last_name_characters.issuperset(lname) and last_name_characters.issuperset(lname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        # return self.last_name + ", " + self.first_name
        return self.last_name + ", " + self.first_name + " has major " + self.major + " " + "with gpa: " + str(self.gpa)

import sys

class Student():
    courseMarks = {}
    name = ""

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        marksSum = 0
        for c in self.courseMarks:
            marksSum += self.courseMarks.get(c)
        return marksSum/len(self.courseMarks)


newStudent = Student("Student", "Family")
print newStudent.name
print newStudent.courseMarks

newStudent.addCourseMark("Biology", 100)
print newStudent.courseMarks

newStudent.addCourseMark("Chemistry", 80)
print newStudent.courseMarks

print newStudent.average()
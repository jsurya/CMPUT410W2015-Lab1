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
    	"""
    	testing:
    	>>> c = Student("A", "Family")

    	>>> c.addCourseMark("Biology", 100)

	>>> c.addCourseMark("Chemistry", 80)

	>>> c.average()
	90
    	"""
        marksSum = 0
        for c in self.courseMarks:
            marksSum += self.courseMarks.get(c)
        return marksSum/len(self.courseMarks)


newStudent = Student("Student", "Family")
print newStudent.name
print newStudent.courseMarks

newStudent.addCourseMark("Biology", 87)
print newStudent.courseMarks

newStudent.addCourseMark("Chemistry", 68)
print newStudent.courseMarks

print newStudent.average()

if __name__ == "__main__":
	import doctest
	doctest.testmod()
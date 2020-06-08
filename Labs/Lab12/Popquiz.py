# Class of students?
# Every student has a first name, middle name, nad a last name.
# Keep in mind, some come from cultures that dont' have middle names. No value.
# every student has a student number, A00123456
# has a GPA
# has a list of classes  that they have passed (can be stored in any form/any data stucture)
# each class has a name, and a final grade
# Student has 3 methods
# First method: get GPA (calcualtes students GPA based on classes they've taken, and RETURNS as a floating point number)
# 2nd method: Get student information which prints out the student's NAME and NUMBER of classes they passed, and their
# cumulative GPA.
# GPA
# RETURNS single string
# 3rd method: Method that allows to change a student's last name (Cause they get married).
# add_course() : Adds a course and puts it to the list

# class level variable: students = A000000000


class Student:
    students = "A00000000"
    studentsCounter = int(students[1:9])

    def __init__(self, firstName, lastName, classList, middleName=""):
        self.__firstName = firstName
        self.__middleName = middleName
        self.__lastName = lastName
        self.__classList = classList
        self.__studentID = Student.students
        Student.studentsCounter += 1
        Student.students = "A" + str(Student.studentsCounter).zfill(8)

    def cum_GPA(self):
        """Calculates GPA

        precondition: classList is a dict
        """
        total = 0
        for key, value in self.__classList.items():
            total += value
        cumGPA = total / len(self.__classList)
        return cumGPA

    def printInfo(self):
        if self.__middleName:
            fullname = self.__firstName + " " + self.__middleName + " " + self.__lastName
        else:
            fullname = self.__firstName + " " + self.__lastName

        classesPassed = 0
        for key, value in self.__classList.items():
            if value >= 50:
                classesPassed += 1
        cumGPA = self.cum_GPA()

        response = (fullname + " passed " + str(classesPassed) + " classes and has a " + str(cumGPA) +
                    " GPA. His/her/zhe student number is " + self.__studentID)
        return response

    def marriage(self):
        self.__lastName = input("Who did you lose your last name to? Enter his/her/zhe last name, please: ").title()
        response = "Your new name is: " + self.__firstName + " " + self.__lastName
        return response


    def removeCourse(self, coursename):
        """Removes a course from the list."""
        if coursename in self.__classList.keys():
            del self.__classList[coursename]
        return "Course removed."


def main():
    classListA = {"COMP1510": 95.0, "COMP1113": 87.0, "COMP1536": 94.0}
    classListB = {"COMM1116": 45.0, "COMP1930": 65.0, "COMP1712": 75.0}
    classListC = {"COMP1510": 37.0, "COMP1712": 40.0, "COMM1116": 0.0}

    studentA = Student("Nicole", "Brooks", classListA, "Page")
    studentB = Student("Cornelius", "Smith", classListB)
    studentC = Student("Harold", "Finch", classListC)

    # Congratulations Nicole!
    # print(studentA.printInfo())
    # # Please enter "Wang" as the new last name.
    # print(studentA.marriage())
    # print(studentA.printInfo())

    #Calculates the GPA
    # print(studentA.cum_GPA())
    # print(studentB.cum_GPA())
    # print(studentA.printInfo())
    # print(studentB.printInfo())

    #Removes the course.
    print(studentA.removeCourse("COMP1510"))
    print(studentA._Student__classList)


if __name__ == "__main__":
    main()

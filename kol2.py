#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


class Diary:

    def __init__(self, student_id, student_name, student_surname):
        self.student_id = student_id
        self.student_name = student_name
        self.student_surname = student_surname
        self.grades_per_subject = {"polish" : [], "english" : [], "math" : []}
        self.attendance = []


    def get_student_name(self):
        return self.student_name, self.student_surname

    def get_total_attendance(self):
        return sum(self.attendance)/len(self.attendance)*100

    def add_grade_per_subject(self, subject, grade):
        self.grades_per_subject[subject].append(grade)
        print "Grade added"

    def add_attendance(self, attendance):
        if attendance == 1:
            self.attendance.append(1)
        if attendance == 0:
            self.attendance.append(0)


    def get_average_score_per_subject(self, subject):
        return sum(self.grades_per_subject[subject])/len(self.grades_per_subject[subject])

    def get_total_average_score(self):
        grades_total_sum = 0
        grades_total_number = 0
        for subject in self.grades_per_subject:
            grades_per_subject = sum(self.grades_per_subject[subject])
            number_of_grades_per_subject = len(self.grades_per_subject[subject])
            grades_total_sum += grades_per_subject
            grades_total_number += number_of_grades_per_subject

        return grades_total_sum/grades_total_number


if __name__ == "__main__":
    janek = Diary(1, "Jan", "Kowalski")
    janek.add_attendance(1)
    janek.add_grade_per_subject("polish", 3)
    grades_average = janek.get_total_attendance()
    print grades_average
    janek.add_attendance(0)



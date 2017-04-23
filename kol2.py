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

# After fix:
# + Have 1 class
# + All data should be in dictionary
#
# + use optparse or argparse
# python module .py -h/arg1/file

# + store user data as json dump
# + path to json dump in argument
# + Print and show me what you got
import json
import optparse


class Diary:
    def __init__(self, json_file):
        self.json_file = json_file
        self.student_attendance = {}
        self.students_grades = {}
        self.students_names = []
        self.__read_json(self.json_file)

    def __read_json(self, json_file):
        with open(json_file) as data_from_json:
            self.json_data = json.load(data_from_json)
        self.subjects = self.json_data["subjects"]
        for student in self.json_data["students"]:
            self.students_names.append(str(student))
            self.student_attendance[str(student)] = self.json_data["students"][student][0]["attendance"]
            for subject in self.subjects:
                self.students_grades[str(student), str(subject)] = self.json_data["students"][student][0][subject][
                    "grades"]

    def get_students_names(self):
        return self.students_names

    def get_total_attendance_of_student(self, student):
        return float(sum(self.student_attendance[student])) / float(len(self.student_attendance[student])) * 100

    def add_grade_per_subject(self, student, subject, grade):
        self.students_grades[student, subject].append(grade)
        print "Grade added"

    def add_attendance(self, student, attendance):
        if attendance == 1:
            self.student_attendance[student].append(1)
        if attendance == 0:
            self.student_attendance[student].append(0)

    def get_average_score_per_subject(self, student, subject):
        return float(sum(self.students_grades[student, subject])) / float(len(self.students_grades[student, subject]))

    def get_total_average_score(self, student):
        average_list = []
        for subject in self.subjects:
            average_list.append(self.get_average_score_per_subject(student, subject))
        return float(sum(average_list)) / float(len(average_list))

    def show_student_details(self, student):
        print "Imie i nazwisko: {}".format(student)
        print "Procentowa obecnosc ucznia: {0:.2f}".format(self.get_total_attendance_of_student(student))
        for subject in self.subjects:
            print "Srednia ocena z przedmiotu {} wynosi {}".format(subject,
                                                                   self.get_average_score_per_subject(student, subject))
        print "Srednia calkowita: {0:.2f}".format(self.get_total_average_score(student))


if __name__ == "__main__":
    parser = optparse.OptionParser("example usage: python kol2 --file PATH_TO_JSON")
    parser.add_option("-f", "--file", dest="file_path",
                      help="provide path to file")
    (options, args) = parser.parse_args()

    file_path = options.file_path
    dziennik_arg = Diary(file_path)
    dziennik = Diary("students_and_grades.json")
    print dziennik.get_students_names()
    ania = "Ania Byk"
    matma = "Math"
    kasia = "Kasia Kos"

    print dziennik.get_total_average_score(ania)
    print dziennik.get_average_score_per_subject(ania, matma)
    print dziennik_arg.get_average_score_per_subject(ania, matma)
    dziennik_arg.show_student_details(ania)
    dziennik.show_student_details(kasia)

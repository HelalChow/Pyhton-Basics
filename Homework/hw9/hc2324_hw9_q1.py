import math as m
class Student:
    def __init__(self, name, NYU_id, net_id):
        self.name = name
        self.NYU_id = NYU_id
        self.net_id = net_id
        self.grades_list = []

    def add_grade(self, catalog_name, grade):
        self.grades_list.append((catalog_name, grade))

    def average(self):
        sum = 0
        for i in self.grades_list:
            sum += int(i[1])
        average = sum/len(self.grades_list)
        return int(round(average, 0))

    def get_email(self):
        return self.net_id+"@nyu.edu"

def load_students(students_data_filename):
    student_list = []
    course = ["", "", "","CS-UY 1114","MA-UY 1024","EG-UY 1001","EG-UY 1003,CS-UY 1122","CS-UY 1134","MA-UY 1124"]
    f = open(students_data_filename, 'r')
    f.readline()
    for line in f:
        line = line.split(',')
        name = line[1]
        NYU_id = line[0]
        net_id = line[2]
        student = Student(name, NYU_id, net_id)
        student_list.append(student)
        for i in range(3,9):
            if line[i] != "":
                student.add_grade(course[i], line[i])
    f.close()
    return student_list

def generate_performance_report(students_lst, out_filename):
    f = open(out_filename, "w")
    print("NYU ID,Average", file = f)
    for i in range(len(students_lst)):
        print(students_lst[i].NYU_id + "," + str(students_lst[i].average()), file = f)
    f.close()

def generate_course_mailing_list(students_lst, catalog_name,out_filename):
    f = open(out_filename, "w")
    for student in students_lst:
        contains_course = False
        for i in student.grades_list:
            if i[0] == catalog_name:
                contains_course = True
        if contains_course == True:
            print(student.get_email(), file = f)
    f.close()

def main():
    course = ["CS-UY 1114", "MA-UY 1024", "EG-UY 1001", "EG-UY 1003,CS-UY 1122", "CS-UY 1134", "MA-UY 1124"]
    student_list = load_students("hw9 - students grades.csv")
    generate_performance_report(student_list, "performance report.txt")
    for i in course:
        fileout = i + " Mailing list.txt"
        generate_course_mailing_list(student_list, i, fileout)

main()

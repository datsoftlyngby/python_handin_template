import names
import random
import string
import matplotlib.pyplot as plt


class Data_sheet:
    

    def __init__(self, courses):
        self.courses = courses
     

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades
    


class Course:
    
    def __init__(self, name, classroom, teacher, ects, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade


class Student:

    course_list = ["Matematik", "Dansk", "Gymnastik", "Fysik"]

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self. data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        my_sum = 0
        grades_list = self.data_sheet.get_grades_as_list()
        for grade in grades_list:
            my_sum += int(grade)
        avg_grade = my_sum / len(grades_list)
        return avg_grade


def generate_students(number):
    course_names = ["Secruity", "Typescript", "Kotlin"]
    genders = ["male", "female"]
    grades = ["-3", "00", "02", "4", "7", "10", "12"]

    for x in range(0, number):
        with open("week3.csv", "a") as file_obj:
            name = names.get_full_name()
            image_url = ''.join(random.choice(string.ascii_lowercase)for i in range(15))
            course = Course(random.choice(course_names),'D klassen', 'Thomas', '20', random.choice(grades))
            data_sheet = Data_sheet([course])
            student = Student(name, random.choice(genders), data_sheet, image_url)
            text_to_file = "name: {stud_name}, gender: {stud_gender} course name: {course_name}, teacher: {teacher}, ects: {ects}, classroom: {classroom}, grade: {grade}, image_url: {image_url}" .format(
                stud_name=student.name, stud_gender=student.gender, course_name=course.name, teacher=course.teacher, ects=course.ects, classroom=course.classroom, grade=course.grade, image_url=student.image_url)
            file_obj.write(text_to_file + "\n")

def sort_students_by_avg_grade(ut):
    newlist = sorted(ut, key=lambda x: x.get_avg_grade(), reverse=True)
    for std in newlist:
        print(std.name)
        print(std.get_avg_grade())
        

def test_read_student_to_list():
    students = []
    with open("week3.csv", "r") as file:
       lines = file.readlines()
       for line in lines:
            print((line.split("ects: "))[1].split(",")[0])
            

def get_students_list():
    student_list = []
    with open("week3.csv", "r") as file_obj:
        lines = file_obj.readlines()
        for line in lines:
          name = (line.split("name: "))[1].split(",")[0]
          course_name = (line.split("course name: "))[1].split(",")[0]
          teacher = (line.split("teacher: "))[1].split(",")[0]
          ects = (line.split("ects: "))[1].split(",")[0]
          classroom = (line.split("classroom: "))[1].split(",")[0]
          grade = (line.split("grade: "))[1].split(",")[0]
          image_url = (line.split("image_url: "))[1].split(",")[0]
          gender = (line.split("gender: "))[1].split(",")[0]

          course = Course(course_name, classroom, teacher, ects, grade)
          data_sheet = Data_sheet([course])
          student = Student(name, gender, data_sheet, image_url)
          student_list.append(student)
    return student_list


def plot_students(students):
    for student in students:
        plt.bar([student.name],[student.get_avg_grade()],width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
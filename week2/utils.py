import os
import csv

def get_file_names(folderpath,out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    file_list = os.listdir(folderpath)
    with open(out, 'a') as file:
        write = csv.writer(file)
        for row in file_list:
            file.write(row + "\n")

get_file_names('/home/jovyan/python_handin_template/week2')



def get_all_file_names(folderpath,out='output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for x in file_names:
        print(x.split(".")[0])

print_line_one(['123.dk','22d.com','123sd.dk'])

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for x in file_names:
        if "@" in x:
            print(x)

print_emails(["asd@asd.com", "asdasd","osteklokke@asd.com"])

def write_headlines(md_files, out='outputExercise2.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    with open(out, 'a') as file:
        for x in md_files:
            with open(x, 'r') as md_file:
                lines = md_file.readlines()
                for line in lines:
                    if line.startswith("#"):
                        file.write(line)

write_headlines(['exercise2.md'])
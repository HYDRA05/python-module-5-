# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
 

file1 = open ('sample.txt.py','r')
reading_file1=file1.read()

print(reading_file1)

file1.close
# file=open(r"C:\Users\divya aghi\PycharmProjects\Python_SDET\FileHandling in python\a1.txt","r")
# print(file.read())
# # print(file.readline())
# # print(file.readable())
# # file.close()
#
# #Appending file
# file=open("a1.txt","a")
# file.write("Now adding more instructions\n")
# file.write("This is easy topic\n")
# file.close()

#Removing file
import os

try:
    os.remove(r"C:\Users\divya aghi\PycharmProjects\Python_SDET\FileHandling in python\a1.txt")
    print("The file is deleted")
except FileNotFoundError as e:
    print(e)
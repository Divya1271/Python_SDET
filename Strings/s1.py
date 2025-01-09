# #Create the string
#
# s="Welcome"
# s=str('Welcome')
# print(s)
#
#Empty string
# name=''
# print(name)
# print(type(name))
#
# #Strings are immutable
# name='Divya'
# print(name)
# name[0]='S'
# print(name)
#
# #id
# message='Welcome'
# print(id(message))
#
# message=message+'to python'
# print(id(message))
#
#+ and * with string
# str="Welcome"
# print(str+"topython")
# print(str*2)
#
# #Slicing in strings
# name="Divya"
# print(name[1:3])
# print(name[:5])
# print(name[2:])
# print(name[1:-1])
# print(name[1:-2])
# print(name[-4:-1])
#
# #ord() and chr()
# print(ord('A'))
# print(ord('B'))
# print(chr(65))
#
# #max(),min() and len()
# print(max('abc'))
# print(max('PQR'))
# print(min('qrs'))
# print(min('aA'))
# print(len("Welcome"))
# print(len([1,2,3,5,6]))
#
# #in,not in in Strings
# s="Welcome"
# print("Wel" in s)
# print("wel" in s)
# print("come" not in s)
#
# #String comparison
# print("Wel"=="Wel")
# print("Free"=="Freedom")
# print("arrow">"arron")
# print("ram">"sham")
# print("Wel">"wel")
#
# #Testing of strings
# s="Divya"
# print(len(s))
# s.isalnum()
# print(s.isalnum())
# print(s.isalpha())
# print('123'.isdigit())
# print(s.isidentifier())
# print('if'.isidentifier())
# print(s.islower())
# print(s.isupper())
# print(" ".isspace())

#Searching in strings
# s='Welcome to python'
# print(s.endswith("Wel"))
# print(s.startswith('Wel'))
#
# #Find
# print(s.find("come"))
# print("hcome".find("hello"))
#
# print(s.count('o'))
# print(s.count(" "))

#Converting
s="today is wednesday"
print(s.capitalize())
print(s.title())
print("MADAM".lower())
print(s.upper())
print(s.swapcase())
print("HELLO".swapcase())
print(s.replace("is","was"))

#Reversing String
# s="Today"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print(rev_str)
# print()
#
# s="Welcome"
# rev_str=s[::-1]
# print(rev_str)

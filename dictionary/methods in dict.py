# mydict={"name":"Anjali","City":"Karnal"}
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# mydictt={"dept":101,"state":"Haryana"}
# mydict.update(mydictt)
# print(mydict)

#copy method
# mydictt=mydict.copy()
# print(mydictt)

#fromkeys(): create the copy of dictionary with specified keys and a single value
# keys=[1,2,3]
# default_value="Welcome"
# mydic=dict.fromkeys([1,2,3,4],"Welcome")
# print(mydic)

#setdefault
# mydict.setdefault("age",30)
# print(mydict)

#iterating the dictionaries
#using for loop
# mydict={"name":"Anjali","City":"Karnal","age":27,"dept":101}
# for i in mydict:
#     print(i)
# for i in mydict.values():
#     print(i)
# for i,j in mydict.items():
#     print(f" {i}:{j}")

#Dictionay comprehension
# {0:0,1:1,2:4,3:9,4:16}
# square={x:x**2 for x in range(0,11)}
# print(square)

#nested dictionary
# mydict={
#     'person1':{'name':'bob','age':29},
#     'person2':{'name':'bunny','age':30}
# }
# print(mydict['person1']['name'])
# print(mydict['person2']['name'])

# union
person1:{'name':'bob','age':29}
person2:{'dept':101,'rollno':30}
result=person1|person2
print(result)
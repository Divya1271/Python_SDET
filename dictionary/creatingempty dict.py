# mydict={}
# print(mydict)

#dictionary with data
# mydict={"name":"Divya","age":23,"class":"Ist"}
# print(mydict)

#using list of tuples
# mydict=dict([("name","Anjali"),("age",27),("address","Haryana")])
# print(mydict)

#using dict constructor
# mydict=dict(name='Bob',age=25)
# print(mydict)

#Using get
# mydict={"name":"Anjali","age":23,"City":"Karnal"}
# print(mydict.get("name"))
# print(mydict.get("age"))
# print(mydict.get("City"))

#using square brackets
# mydict={"name":"Anjali","age":23,"City":"Karnal"}
# print(mydict["name"])
# print(mydict["age"])


mydict={"name":"Anjali","age":23,"City":"Karnal"}
# print(f"The value of name before updation: {mydict}")
# mydict["name"]="Divya"
# print(f"The value of name after updation: {mydict}")

mydict={"name":"Anjali","age":23,"City":"Karnal"}
del mydict["age"]
print(mydict)

#pop
mydict.pop("name")
print(mydict)

#popitem
mydict.popitem()
print(mydict)
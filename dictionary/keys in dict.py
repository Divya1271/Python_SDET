mydict={"name":"Divya","age":23,"dept":101,"rollno":101}
# value=input("Enter the value for which you want to fetch the keys ")
value=101
# ans=mydict.items()
# print(ans)
for i,j in mydict.items():
    # print(i,j)
    if j==value:
       print(i,end=" ")




city=['Kaithal','karnal','Yamunanagar','Kota','Saharanpur']
def length(city):
    return len(city)
sort=sorted(city,key=length,reverse=False)
print(sort)

sort=sorted(city,key=lambda x:len(x),reverse=False)
print(sort)
Mydic={"Apple":100,"Banana":200,"Orange":300}
# name=input("Enter the name of the fruit")
try:
    name = input("Enter the name of the fruit")
    for i,j in Mydic.items():
        if i==name:
            print(j)
    # else:
    #     print("Fruit not present in the dictionary")
except Exception as e:
    print(e)





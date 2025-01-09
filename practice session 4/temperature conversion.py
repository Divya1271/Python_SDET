n=int(input("Enter the temperature in degrees"))
cel=0
far=0
print("1.Conversion from celcius to farenheit")
print("2.Conversion from farenheit to celcius")
choice=int(input("Enter the type of conversion 1 or 2"))
if(choice==1):
    cel=(n*9/5) + 32
    print("The temperature in farenheit is",cel)
elif(choice==2):
    far=(n*5/9) - 32
    print("The temperature in celcius is",far)
else:
    print("Invalid conversion")





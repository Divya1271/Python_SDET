import math
num=int(input("Enter the number"))
try:
    ans = math.sqrt(num)
    print(ans)
except Exception as e:
    print(e)

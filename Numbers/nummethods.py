#abs
print(abs(3.4))
print(abs(-5))

#Roundof
print(round(4.1546,3))
print(round(4.5))

#pow

print(pow(2,3))
print(pow(5,2))

#min
print(min(2,6,7,1))
print(max(2,6,7,1,9))

#sum
print(sum([1,3,5,7]))
print(sum((2,3,4,5)))

#divmod....it will return a tuple 1 is quotient and 2 is remainder
print(divmod(10,3))

#complex
print(complex(1,2))
print(complex(3))

#isinstance....whether the value is the instance of this class or not
print(isinstance(5,int))
print(isinstance(3.14,float))

#factorial
import math
number=7
result=math.factorial(number)
print(f"Factorial of {number} is {result}")
# def sum_of_digits(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum+=rem
#         n=n//10
#     return sum
# print(sum_of_digits(985))

def sum_of_digits(n):
    if n<1:
        return 0
    else:
        return n%10+sum_of_digits(n//10)
print(sum_of_digits(985))

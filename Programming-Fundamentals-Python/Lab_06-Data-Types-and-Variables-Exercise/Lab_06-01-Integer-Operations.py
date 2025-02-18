# 1. Integer Operations
# Write a program that reads four integer numbers.
# It should add the first to the second number,
# integer divide the sum by the third number,
# and multiply the result by the fourth number.
# Print the final result.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num3 != 0:
    result=int((num1+num2)//num3*num4) # integer divide je celobrojno deljenje
    print(result)
else:
    pass

# TIPS
# Celobrojno deljenje se na engleskom naziva "integer divide".
# Deljenje sa ostatkom se na engleskom naziva "modulus operation"
# ili jednostavno "modulo".
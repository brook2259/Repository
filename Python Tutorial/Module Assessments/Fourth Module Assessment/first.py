# Calculate Factorial Using Recursion

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        result = num*factorial(num-1)
    return result


num=5

result = factorial(num)

print('the factorial of num is: ', result)
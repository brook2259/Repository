def main():
    factorial = int(input('Enter an integer to find its factorial: '))
    
    fact = 1  
    x = factorial
    
    while x > 1:  
        fact *= x  
        x -= 1  
        
    print('The factorial of ', factorial, 'is ',fact)  #
    return fact

main()
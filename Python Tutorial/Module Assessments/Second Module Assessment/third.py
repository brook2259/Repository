def main():
    
    num = int(input('please enter a whole number:'))

    for i in range(2,num):
   
        even = i %2 == 0
        three = i %3 == 0
        five = i%5 ==0
        if even == False:
            if i <=3 or three == False:
                if i <=5 or five == False:
                    print(i)
main()
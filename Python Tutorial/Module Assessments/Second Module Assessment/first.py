def main():
    f0 = int(input('enter either 0 or 1:'))
    f1 = int(input('enter the number that follows the number you just entered:'))
    final = int(input('how many fibonacci values would you like to generate? '))
    f2 = [f0,f1]
    
    for index in range(2,final):
        fn = f2[index-1]+f2[index-2]
        f2.append(fn)
    print(f2)
    return f2
main()
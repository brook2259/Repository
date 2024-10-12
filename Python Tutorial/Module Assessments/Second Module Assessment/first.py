def main():
    f0 = int(input('enter either 0 or 1:'))
    f1 = int(input('enter the number that follows the number you just entered:'))
    f2 = [f0,f1]
    
    for index in range(2,10):
        fn = f2[index-1]+f2[index-2]
        f2.append(fn)
    print(f2)
    return f2
main()
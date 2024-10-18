def calc_avg():
    
    lst1 = []
    lst1 = [int(item) for item in input("Enter \
                the list items : ").split()]


    avg = sum(lst1)/len(lst1)
    #print(lst1)
    print(avg)
    return avg

calc_avg()
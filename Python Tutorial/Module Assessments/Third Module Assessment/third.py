def main():
    arr = (input("enter the array:"))
    number_list = arr.split()
    number_list = list(map(int, number_list))
    arr = number_list


    length = len(arr)
    if length <= 1:
        print(arr)
    for i in range(1,length):
        current = arr[i]
        j= i-1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    print(arr)
    return arr
    
main()
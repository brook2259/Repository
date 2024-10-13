def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  # Find the middle index
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half
    
    return merge(left_half, right_half)  # Merge the sorted halves

# Convert a string of random numbers to a list
#number_string = "34 2 42 15 8"


import random

ls = random.sample(range(1, 50), 8)
ls1 = ','.join(map(str, ls))
number_list = list(map(int, ls1.split(',')))  # Split and convert to integers

# Sort the list
sorted_numbers = merge_sort(number_list)
print(f'Sorted List: {sorted_numbers}')


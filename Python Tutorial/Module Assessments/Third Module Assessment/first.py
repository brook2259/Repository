import random

ls = random.sample(range(1, 50), 7)

for i in range(len(ls)):
    for num in range(len(ls)-1):
        if ls[num] > ls[num+1]:
            ls[num],ls[num+1] = ls[num+1], ls[num]
        #print(ls)
print(ls)
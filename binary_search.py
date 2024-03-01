import random
import time

#in this code we have a sorted list will compare between naive search and binary search

def main():
    length = 1000
    #sorted list
    sorted_list = set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    
    #calculating the intervall for binary search for every single item of the list
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f"binary search took {(end - start)/length} seconds to complete")

        #calculating the intervall for naive search for every single item of the list
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f"naive search took {(end - start)/length} seconds to complete")



#naive search iterate through the list until the target is found
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

#binary search
def binary_search(l, target, low=None, high=None):
    midpoint = 0
    if high==None:
        high = len(l)-1
    if low == None:
        low = 0
    
    if high<low:
        return -1

    midpoint = (high + low) // 2

    if l[midpoint ] == target:
        return midpoint 
    elif l[midpoint ] < target:
        binary_search(l, target, midpoint+1, high)
    else:
        binary_search(l, target, low, midpoint-1)

if __name__== "__main__":
    main()
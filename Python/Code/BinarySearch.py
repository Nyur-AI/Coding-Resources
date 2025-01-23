def binary_search(l, num):
    low = 0
    high = len(l)-1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        if num == l[mid]:
            return mid
        elif num >= l[mid]:
            low = mid + 1
        elif num <= l[mid]:
            high = mid - 1
        else:
            print("Number not found")
    
    return -1

l = [0, 1, 2, 3, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]
num = 16
print(binary_search(l, num))

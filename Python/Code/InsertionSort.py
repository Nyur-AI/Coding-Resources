def insertion_sort(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = a
    return arr

arr = [3,1,2,5,4,6,9,8,7,0]

print(insertion_sort(arr))

"""
Time Complexity :
    - Worst Case : O(n^2) 
    - Best Case : 0(n)
Space Complexity : O(1)
"""

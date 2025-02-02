def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # No swaps = already sorted
            break
    return arr

arr = [3,1,2,5,4,6,9,8,7,0]

print(bubble_sort(arr))


"""
Time Complexity :
    - Worst Case : O(n^2) 
    - Best Case : 0(n)
Space Complexity : O(1)
"""
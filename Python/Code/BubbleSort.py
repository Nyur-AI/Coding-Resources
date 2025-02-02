def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i- 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [3,1,2,5,4,6,9,8,7,0]

print(bubblesort(arr))


"""
Time Complexity :
    - Worst Case : O(n^2) 
    - Best Case : 0(n)
Space Complexity : O(1)
"""
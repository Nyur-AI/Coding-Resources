def selectionsort(arr):
    n = len(arr)

    for s in range(n):
        min_idx = s

        for i in range(s + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])
    
    return arr


arr = [3,1,2,5,4,6,9,8,7,0]

print(selectionsort(arr))

"""
Time Complexity :
    - Worst Case : O(n^2) 
    - Best Case : 0(n^2)
Space Complexity : O(1)
"""


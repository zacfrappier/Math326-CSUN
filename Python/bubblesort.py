# Optimized Python program for implementation of Bubble Sort
#Geeksforgeeks
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(arr)
        if (swapped == False):
            break

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 90, 12, 90, 11, 22]
    print(arr)
    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

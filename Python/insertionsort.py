# Python program for implementation of Insertion Sort
#Geeksforgeeks
# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:          
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
            print(arr)
        #arr[j + 1] = key

# Driver method
if __name__ == "__main__":
    arr = [64, 34, 25, 90, 12, 90, 11, 22]
    print(arr)
    insertionSort(arr)
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    # This code is contributed by Hritik Shah.

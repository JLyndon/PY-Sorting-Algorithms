# -------------------- QUICK SORT --------------------------
# Code snippet from geeksforgeeks.org

# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# Function to perform Quick Sort
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)  # Recursive >>> Left
        quickSort(array, pi + 1, high) # Recursive >>> Right

data = [93, 57, 76, 21, 95, 69, 51, 74, 38, 63]
n = len(data)

print("\n\u001b[36mUnsorted Array\u001b[0m")
print(data)

print("\n\u001b[32mSorted Array\u001b[0m in Ascending Order:")

quickSort(data, 0, n - 1)
print(data, "\n")
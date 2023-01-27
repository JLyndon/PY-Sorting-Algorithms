# -------------------- INSERTION SORT --------------------------
# Code snippet from programiz.com

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

data = [93, 57, 76, 21, 95, 69, 51, 74, 38, 63]

print("\n\u001b[36mUnsorted Array\u001b[0m")
print(data)

print("\n\u001b[32mSorted Array\u001b[0m in Ascending Order:")
print(insertionSort(data), "\n")
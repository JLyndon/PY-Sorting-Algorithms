# -------------------- INSERTION SORT --------------------------
# Code snippet from geeksforgeeks.org

def insertionSort(array):
    if (n := len(array)) <= 1:
      return
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key

data = [93, 57, 76, 21, 95, 69, 51, 74, 38, 63]

print("\n\u001b[36mUnsorted Array\u001b[0m")
print(data)

print("\n\u001b[32mSorted Array\u001b[0m in Ascending Order:")

insertionSort(data)
print(data, "\n")
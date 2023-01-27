# -------------------- SELECTION SORT --------------------------
# Code snippet from guru99.com

def selectionSort(itemsList):
    n = len(itemsList)
    for i in range(n - 1): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList

data = [93, 57, 76, 21, 95, 69, 51, 74, 38, 63]

print("\n\u001b[36mUnsorted Array\u001b[0m")
print(data)

print("\n\u001b[32mSorted Array\u001b[0m in Ascending Order:")
print(selectionSort(data), "\n")
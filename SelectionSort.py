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


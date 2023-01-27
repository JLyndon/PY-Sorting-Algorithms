# -------------------- BUBBLE SORT --------------------------
# Code snippet from guru99.com

def bubbleSort(pdata):
    n = len(pdata)

    for i in range(n - 1) :
        flag = 0
        for j in range(n - 1) :
            if pdata[j] > pdata[j + 1] : 
                tmp = pdata[j]
                pdata[j] = pdata[j + 1]
                pdata[j + 1] = tmp
                flag = 1
        if flag == 0:
            break

    return pdata

data = [93, 57, 76, 21, 95, 69, 51, 74, 38, 63]

print("\n\u001b[36mUnsorted Array\u001b[0m")
print(data)

print("\n\u001b[32mSorted Array\u001b[0m in Ascending Order:")
print(bubbleSort(data), "\n")
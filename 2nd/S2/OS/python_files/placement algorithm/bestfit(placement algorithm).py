
def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j

        if bestIdx != -1:
            allocation[i] = bestIdx

            blockSize[bestIdx] -= processSize[i]

    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(i + 1, "\t\t", processSize[i], end=" \t\t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

blockSize = [75,175]
processSize = [25,50,100,75]
m = len(blockSize)
n = len(processSize)
bestFit(blockSize, m, processSize, n)
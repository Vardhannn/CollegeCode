def FirstFit(block_Size, m, process_Size, n):
    allocate = [-1] * n


    for i in range(n):
        for j in range(m):
            if block_Size[j] >= process_Size[i]:
                allocate[i] = j

                block_Size[j] -= process_Size[i]
                break

    print("Process No.\t\tProcess\t\t   Size Block No.")

    for i in range(n):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")


# Driver code

block_Size = [75,175]
process_Size = [25,50,100,75]
m = len(block_Size)
n = len(process_Size)

FirstFit(block_Size, m, process_Size, n)
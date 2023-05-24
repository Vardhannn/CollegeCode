import sys

def Mindenom(Notes, m, sumreq):
    
    table = [0 for i in range(sumreq + 1)]

    table[0] = 0

    for i in range(1, sumreq + 1):
        table[i] = sys.maxsize

    for i in range(1, sumreq + 1):

        for j in range(m):
            if (Notes[j] <= i):
                sub_res = table[i - Notes[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[sumreq] == sys.maxsize:
        return -1

    return table[sumreq]

if __name__ == "__main__":

    Notes = [500,200,100,50,20,10]
    m = len(Notes)
    sumreq = 420
    print("Minimum Notes required is ",
                Mindenom(Notes, m, sumreq))

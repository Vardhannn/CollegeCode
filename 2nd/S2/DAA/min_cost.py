def min_cost_rods(S, r1, c1, r2, c2):

    S.sort()
    rods_used = []
    total_cost = 0
    i = len(S) - 1
    while i >= 0:
        if i >= 1 and S[i] <= r1 and S[i-1] <= r1:
            rods_used.append((1, r1))
            total_cost += c1
            i -= 2
        elif S[i] <= r2:
            
            rods_used.append((2, r2))
            total_cost += c2
            i -= 1
        else:
            return -1, []
    rods_used.reverse()
    return total_cost, rods_used


def main():
    
    r1, c1 = map(int, input("Enter the length and cost of type 1 rod (r1 c1): ").split())
    r2, c2 = map(int, input("Enter the length and cost of type 2 rod (r2 c2): ").split())
    S = list(map(int, input("Enter the cut pieces S: ").split()))

    min_cost, rods_used = min_cost_rods(S, r1, c1, r2, c2)
    if min_cost == -1:
        print("It is not possible to accommodate all cut pieces.")
    else:
        print("Minimum cost to accommodate all cut pieces:", min_cost)
        for i, rod in enumerate(rods_used):
            print("Rod used for cut piece {}: type {}, length {}".format(i+1, rod[0], rod[1]))


if __name__== '__main__':
    main()

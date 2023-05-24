def worstfit(b_size, m, p_size, n): 

    allocate = [-1] * n 
    for i in range(n):
        wstIdx = -1
        for j in range(m): 
            if b_size[j] >= p_size[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif b_size[wstIdx] < b_size[j]:  
                    wstIdx = j 
    
        if wstIdx != -1:
            allocate[i] = wstIdx  
            b_size[wstIdx] -= p_size[i] 
    print ("Process Number Process Size Block Number") 
    for i in range(n): 
        print(i + 1, "       ",p_size[i], end = "    ")  
        if allocate[i] != -1: 
            print(allocate[i] + 1)  
        else:
            print("Not Allocated") 

 
     
# Driver code
if __name__ == '__main__': 
    b_size = [75,175]  
    p_size = [25,50,100,75]  
    m = len(b_size)  
    n = len(p_size)  
  
    worstfit(b_size, m, p_size, n)

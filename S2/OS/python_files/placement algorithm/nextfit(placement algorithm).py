
def Next_fit(block_size, m, process_size, n):
    allocate = [-1] * n  
    j = 0     
    for i in range(n): 
        while j < m: 
            if block_size[j] >= process_size[i]: 
                allocate[i] = j 
                block_size[j] -= process_size[i]  
                break
            j = (j + 1) % m 
            
    print("Process No. Process Size Block no.")  
    for i in range(n): 
        print(i + 1, "         ", process_size[i],end = "     ") 
        if allocate[i] != -1: 
            print(allocate[i] + 1)  
        else: 
            print("Not Allocated") 
  
 # Driver Code 
if __name__ == '__main__':  
    block_size = [75,175] 
    process_size = [25,50,100,75]
    m = len(block_size) 
    n = len(process_size) 
  
    Next_fit(block_size, m, process_size, n)

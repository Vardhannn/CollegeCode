def min_time_to_process_jobs(a, b):
    n = len(a)
    T = [[0 for j in range(2)] for i in range(n)]
    x=['Null']*n
    T[0][0] = a[0]
    T[0][1] = b[0]
    
    for i in range(1, n):
        
        T[i][0] = min(T[i-1][1] + b[i], T[i-1][0] + a[i])
        T[i][1] = min(T[i-1][0] + a[i], T[i-1][1] + b[i])
    print(T)
  
    return min(T[n-1][0], T[n-1][1])

a = [5, 2, 6, 11]
b = [3, 4, 2, 6]
print(min_time_to_process_jobs(a, b))

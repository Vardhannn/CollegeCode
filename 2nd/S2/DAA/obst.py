def obst(p, q, n):
    cost = [[0 for j in range(n+1)] for i in range(n+2)]
    weight = [[0 for j in range(n+1)] for i in range(n+2)]
    root = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+2):
        cost[i][i-1] = q[i-1]
        weight[i][i-1] = q[i-1]
        
    for L in range(1, n+1):
        for i in range(1, n-L+2):
            j = i + L - 1
            cost[i][j] = 99999
            weight[i][j] = weight[i][j-1] + p[j-1] + q[j]
            for r in range(i, j+1):
                temp = cost[i][r-1] + cost[r+1][j] + weight[i][j]
                if temp < cost[i][j]:
                    cost[i][j] = temp
                    root[i][j] = r
    return (cost, root, weight)

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def build_obst(keys,q,root,i,j):
    if i > j:
        return None
    key = keys[root[i][j]]
    node = Node(key)
    node.left=build_obst(keys,q,root,i,root[i][j]-1)
    node.right=build_obst(keys,q,root,root[i][j]+1, j)  
    return node

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)
p=[0.5,0.1,0.05]
q=[0.15,0.1,0.05,0.05]
n=len(p)
keys=['if','do','while']
cost, root, weight = obst(p, q, n)
root_node=build_obst(keys, q, root, 0, n-1)
print(cost[1:])
print(root[1:])
print(weight[1:])
inorder(root_node)

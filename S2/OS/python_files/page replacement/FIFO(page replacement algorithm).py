#First in first out(FIFO)

l=list(map(int,input("enter page numbers :").split()))
n=int(input("enter no of frames : "))
print("Pages :")
b=[]
q=0
count=0
for i in l :
    if len(b)<n and i not in b :
        b.append(i)
        print(b)
        count+=1
    elif len(b)>=n and i not in b :
        if q>n-1:
            q=0
            b.pop(q)
            b.insert(q,i)
            q=q+1
            print(b)
            count+=1
        else:
            b.pop(q)
            b.insert(0,i)
            q=q+1
            print(b)
            count+=1
print("Number of page defaults : ",count)
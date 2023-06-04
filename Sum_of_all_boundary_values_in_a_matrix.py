a,b=map(int,input().split())
m=[]
s=0
for i in range(a): 
    u=list(map(int,input().split()))
    m.append(u)
for i in range(a):
    for j in range(b):
        if i==0 or i==a-1:
            s+=m[i][j]
        elif j==0 or j==b-1:
            s+=m[i][j]
print(s)
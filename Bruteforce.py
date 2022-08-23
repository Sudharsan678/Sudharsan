from itertools import combinations_with_replacement as string
m=list(map(int,input().split()))
n=int(input())
li=[]
for x in range(1,n+1):
    li.append(string(m,x))
t=[]
for x in li:
    for y in x:
        if sum(y) == n:
            t.append(y)
print(t)
print(t[0])

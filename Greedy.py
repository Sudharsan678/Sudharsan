m=list(map(int,input().split()))
n=int(input())
count=0
li=[]
temp=[]
while n!=0:
    if n >= m[-1]:
        n = n-m[-1]
        count = count+1
    if n < m[-1]:
        li.append(m.pop())
temp=temp.append(n)
print(temp[0])
print(count)
n=list(map(int,input().split(" ")))
lst=list(map(int,input().split(" ")))
a=set(map(int,input().split(" ")))
b=set(map(int,input().split(" ")))
sum=0
for i in lst:
    if i in a:
        sum+=1
    if i in b:
        sum-=1
print(sum)

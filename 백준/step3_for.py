# 구구단 

dan=int(input())

for i in range(1,10):
    print(dan, '*',i,'=',dan*i)


#  A+B - 3
n=int(input())
lst1=[]
lst2=[]
for i in range(n):
    a,b=map(int, input().split())
    lst1.append(a)
    lst2.append(b)

for a,b in zip(lst1,lst2):
    print(a+b)


#  합 
num=int(input())
result=0
for i in range(1,num+1):
    result+=i
print(result)

# 빠른 A+B
import sys
n=int(input())
lst1=[]
lst2=[]
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    lst1.append(a)
    lst2.append(b)
for a,b in zip(lst1,lst2):
    print(a+b)

# N 찍기
n= int(input())
for i in range(1,n+1):
    print(i)


#  기찍 N
n= int(input())
for i in range(n,0,-1):
    print(i)


#  A+B - 7
import sys
lst=[]
n= int(input())
for i in range(n):
    a,b=map(int,input().split())
    lst.append(a+b)

for i,result in enumerate(lst):
    print("Case #%d: %d" %(i+1,result))


# A+B - 8
import sys
lst1=[]
lst2=[]
n= int(input())
for i in range(n):
    a,b=map(int,input().split())
    lst1.append(a)
    lst2.append(b)

for i,r in enumerate(zip(lst1,lst2)):
    print("Case #%d: %d + %d = %d" %(i+1,r[0],r[1],r[0]+r[1]))

# 별 찍기
n=int(input())
for i in range(1,n+1):
    print('*'*i)

# 별찍기 2
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),'*'*i,sep='')

# X보다 작은 수
N,X=map(int, input().split())
lst=list(map(int,input().split()))

for i in lst:
    if X > i:
        print(i, end=' ')
def solution1():
    n=int(input())
    lst=list(map(int,input().split()))
    print(min(lst),max(lst))
# solution1()


def solution2():
    lst=[]
    while True:
        try:
            num=int(input())
            lst.append(num)
        except:
            break
    print(max(lst))
    print(lst.index(max(lst))+1)
# solution2()


def solution3():
    a=int(input())
    b=int(input())
    c=int(input())

    resultInt=a*b*c
    resultString=str(resultInt)
    print(resultString)
    for i in range(0,10):
        print(resultString.count(str(i)))
# solution3()


def solution4():
    lst=[]
    while True:
        try:
            lst.append(int(input())%42)
        except:
            break
    result=len(set(lst))
    print(result)
# solution4()

def solution5():
    n=int(input())
    lst=list(map(int,input().split()))
    m=max(lst)
    for i in range(n):
        lst[i]=(lst[i]/m)*100
    print(sum(lst)/n)
# solution5()

def solution6():
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(input())
    for str in lst:
        count=0
        temp=0
        for s in str:
            if s=='O':
                temp+=1
                count+=temp
            else:
                temp=0
        print(count)
# solution6()


def solution7():
    n=int(input())
    for i in range(n):
        count=0
        lst=list(map(int, input().split()))
        lst2=[i for i in lst[1:] if i>sum(lst[1:])/lst[0]]
        print("{:.3f}%".format(len(lst2)/lst[0]*100))
solution7()

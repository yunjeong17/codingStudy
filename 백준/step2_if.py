#윤년
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

def yoon(year):
    if(year%4==0 and (year%100!=0 or year%400==0) ):
        return 1
    else:
        return 0

year=int(input())
print(yoon(year))


#사분면
def quadrant(x,y):
    if x>0:
        if y>0:
            return 1
        else:
            return 4
    else:
        if y>0:
            return 2
        else:
            return 3

x=int(input())
y=int(input())
print(quadrant(x,y))    

# 알람 시계
def timer(h,m):
    if m>=45:
        m-=45
    elif h>0:
        m=15+m
        h-=1
    else :
        m=15+m
        h=23
    print(h,m) 

h,m=map(int,input().split())
timer(h,m)

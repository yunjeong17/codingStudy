# 10172 개
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\ ')
print('|"^"`    |')
print('||_/=\\\__|')


# #A X B
a,b=map(int,input().split())
print(a*b)

# # A / B
a,b=map(int,input().split())
print(a/b)

# 사칙연산
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)


# 나머지
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력
A,B,C = map(int,input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

# 곱
a = int( input())
b= int(input())

b1= b%10
b2= (b%100-b1)//10
b3= b//100
print(a*b1, a*b2, a*b3, a*b, sep="\n")

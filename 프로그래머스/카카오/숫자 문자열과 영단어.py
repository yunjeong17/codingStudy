# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301
import re

# 같은 숫자가 안나온다면 이렇게 해도 되는데 같은 숫자가 영어로 되어있을 가능성이 있음
def solution1(s):
    answer = 0
    num={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for i in num.keys():
        findI=s.find(i)
        if findI != -1 :
            s=s[:findI]+str(num[i])+s[findI+len(i):]
    return s

# 그냥 다.. replace 해버리자...
def solution2(s):
    answer = 0
    num={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for a,b in num.items():
        s=s.replace(a,b)
    return int(s)


print(solution2("one4seveneight"),"result:1478")
# print(solution1("23four5six7"),"result:234567")
# print(solution1("2three45sixseven"),"result:234567")
# print(solution2("123"),"result: 123")
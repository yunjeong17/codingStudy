# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

# 이차원리스트를 딕셔너리로 변경
# clothes[][1]을 key로 clothes[][0]을 value로 해서 
from itertools import combinations

#하긴했는데 엄청나게 느림....
def solution1(clothes):
    answer =0
    # 리스트 > 딕셔너리
    dic ={}
    for c in clothes:
        if c[1] in dic.keys():
            lst=dic[c[1]]
            lst.append(c[0])
            dic[c[1]]=lst
        else:
            dic[c[1]]=[c[0]]

    for k,v in dic.items():
        dic[k]=len(v)
    print(dic)

    result=1
    for i in range(0,len(dic.keys())): 
        for j in combinations(list(dic.values()), i+1):
            for k in range(i+1):
                result*=j[k]
            answer+=result
            result=1
    return answer


#완전 혁신적... 배워야지... 무조건 순차적 프로그래밍 하지말고 결과 중심으로 해볼 것.
#다른 방법 : 다른 사람 풀이법 참고
# https://programmers.co.kr/questions/15225
# 내가 잘못된 풀이로 하고있었구나... 
def solution2(clothes):
    # 리스트 > 딕셔너리
    dic ={}
    result=1
    for c in clothes:
        if c[1] in dic.keys():
            lst=dic[c[1]]
            lst.append(c[0])
            dic[c[1]]=lst
        else:
            dic[c[1]]=[c[0]]
    print(dic)
    for v in dic.values():
        result*=(len(v)+1) # 종류의 개수 +안입은거
    result-=1 #전부 안입은거 -1
    return result

print(solution2([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]), "   result:5")
print(solution2([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]), "   result:3")
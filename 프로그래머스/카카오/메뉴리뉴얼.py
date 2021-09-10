# 문제 : 메뉴리뉴얼
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/72411

# ㅎㅎ 지저분하지만 풀었당 ㅎㅎㅎ
from itertools import combinations
def solution(orders, course):
    answer = []
    tempOrder=[dict() for i in course]
    print(tempOrder)
    for i in range(len(course)):
        for j in orders:
            if combinations(j, course[i]):
                t=list(combinations(j, course[i]))
                print(tempOrder[i])
                for k in t:
                    listK=list(k)
                    listK.sort()
                    print(listK)
                    str=''.join(listK)
                    if str in tempOrder[i]:
                        tempOrder[i][str]=tempOrder[i][str]+1
                    else:
                        tempOrder[i][str]=1
    print(tempOrder)
    
    for tempDict in tempOrder:
        answer+=[k for k,v in tempDict.items() if max(tempDict.values()) == v and v>1 ]

    answer.sort()
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]),'result:["AC", "ACDE", "BCFG", "CDE"]')
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]),'result: ["ACD", "AD", "ADE", "CD", "XYZ"]')
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]),'result:["WX", "XY"]')
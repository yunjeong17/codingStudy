# 문제 : 후보키
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations #조합

def solution(relation):
    answer = 0
    lst=list(zip(*relation))
    print(lst)
    comlst=[]
    for i in range(1,len(lst)+1):
        comlst+=list(combinations( [k for k in range(len(lst))],i))
        print(comlst)
                

    return answer


#result:2
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
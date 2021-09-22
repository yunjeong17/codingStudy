# 문제 : 프린터
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
def solution(priorities, location):
    answer = 0
    lst=[i for i in range(len(priorities))]
    final=[]
    while len(priorities)!=0:
        if priorities[0]!=max(priorities):
            priorities.append( priorities.pop(0) )
            lst.append(lst.pop(0))
        else:
            priorities.pop(0)
            final.append( lst.pop(0) )
    
    answer=final.index(location)+1
    return answer

print(solution([2, 1, 3, 2],2),'result:1')
# print(solution([1, 1, 9, 1, 1, 1],0),'result:5')

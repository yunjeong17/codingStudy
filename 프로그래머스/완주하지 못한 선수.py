#완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576

import collections
from collections import Counter

def solution(participant, completion):
    p={}
    c={}
    for item in participant:
        if item not in p:
            p[item]=0
        if item in p:
            p[item]=p.get(item)+1
            
    for i in completion:
        if i not in c:
            c[i]=0
        if i in c:
            c[i]=c.get(i)+1
    result="".join(Counter(p)-Counter(c))
    return result
        
#participant=["leo", "kiki", "eden","kayo","kam"]
participant=["mislav", "stanko", "mislav", "ana"]
#completion=["eden", "kiki"]
completion=["stanko", "ana", "mislav"]

def solution2(participant, completion):    
    print(collections.Counter(participant))
    answer= collections.Counter(participant)-collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]

print(solution(participant,completion))
print("----------------")
print(solution2(participant,completion))

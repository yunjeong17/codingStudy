# 문제 : 순위검색
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/72412

# 언어	    직군	    경력	    소울 푸드	 점수
# java  	backend	    junior	    pizza	    150
# python	frontend	senior	    chicken	    210
# python	frontend	senior  	chicken	    150
# cpp	    backend	    senior  	pizza	    260
# java  	backend	    junior  	chicken 	80
# python	backend 	senior  	chicken	    50

import re
from collections import Counter
def solution(info, query):
    answer = []
    infoList=[]
    queryList=[]

    for i in info :
        lst=i.split(" ")
        infoDict={j:-1 for j in lst[:-1]}
        infoDict["score"]=int(lst[-1])
        infoList.append(infoDict)

    for q in query:
        lst= re.split(" and | ",q)
        queryDict={j:1 for j in lst[:-1]}
        queryDict["score"]=-int(lst[-1])+1
        if '-' in queryDict:
            del queryDict['-']
        queryList.append(queryDict)

    print("infoList",infoList)
    print("queryList",queryList)
    print("============================")

    for que in queryList:
        print("query",que)
        cnt=0
        for inf in infoList:
            print("info",inf)
            print(Counter(que)+Counter(inf))
            if len(Counter(que)+Counter(inf))==1 and "score" in (Counter(que)+Counter(inf)) :
                cnt+=1
                print("wow!!",cnt)
        print("===========================")
        answer.append(cnt)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),"result:[1,1,1,1,2,4]")
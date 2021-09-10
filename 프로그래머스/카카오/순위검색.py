# # 문제 : 순위검색
# # 링크 : https://programmers.co.kr/learn/courses/30/lessons/72412

# # 언어	    직군	    경력	    소울 푸드	 점수
# # java  	backend	    junior	    pizza	    150
# # python	frontend	senior	    chicken	    210
# # python	frontend	senior  	chicken	    150
# # cpp	    backend	    senior  	pizza	    260
# # java  	backend	    junior  	chicken 	80
# # python	backend 	senior  	chicken	    50






# # 정확성은 100점인데..ㅠㅠ 효율성 0점이네...
# import re
# from collections import Counter
# def solution(info, query):
#     answer = []
#     infoList=[]
#     queryList=[]

#     for i in info :
#         lst=i.split(" ")
#         infoDict={j:-1 for j in lst[:-1]}
#         infoDict["score"]=int(lst[-1])
#         infoList.append(infoDict)

#     for q in query:
#         lst= re.split(" and | ",q)
#         queryDict={j:1 for j in lst[:-1]}
#         queryDict["score"]=-int(lst[-1])+1
#         if '-' in queryDict:
#             del queryDict['-']
#         queryList.append(queryDict)

#     print("infoList",infoList)
#     print("queryList",queryList)
#     print("============================")

#     for que in queryList:
#         print("query",que)
#         cnt=0
#         for inf in infoList:
#             print("info",inf)
#             print(Counter(que)+Counter(inf))
#             if len(Counter(que)+Counter(inf))==1 and "score" in (Counter(que)+Counter(inf)) :
#                 cnt+=1
#                 print("wow!!",cnt)
#         print("===========================")
#         answer.append(cnt)
#     return answer


# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),"result:[1,1,1,1,2,4]")

# # #딕셔너리 안쓰고 했는데 효율성 딱히 뭐.,......... 엄청나게 바뀌진않네....
# def solution2(info, query):
#     answer = []
#     infoList=[]
#     queryList=[]

#     for i in info :
#         lst=i.split(" ")
#         infoList.append(lst)

#     for q in query:
#         lst= [_ for _ in q.split(' ') if _ != 'and' and _ !='-']
#         queryList.append(lst)
    
#     for q in queryList:
#         cnt=0
#         for i in infoList:
#             if int(q[-1])>int(i[-1]) or len(Counter(q[:-1])-Counter(i[:-1]))!=0:
#                 continue
#             cnt+=1
#         answer.append(cnt)

#     return answer


# #이것도 막 엄청나게,,,, 효율성이 올라가진 않음..
# from collections import Counter
# def solution3(info, query):
#     answer = []
#     infoList=[]

#     for i in info :
#         lst=i.split(" ")
#         infoList.append(lst)

#     for q in query:
#         lst= [_ for _ in q.split(' ') if _ != 'and' and _ !='-']
#         cnt=0
#         for i in infoList:
#             if int(lst[-1])>int(i[-1]) or len(Counter(lst[:-1])-Counter(i[:-1]))!=0:
#                 continue
#             cnt+=1
#         answer.append(cnt)

#     return answer
# # print(solution2(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),"result:[1,1,1,1,2,4]")


# # # 앞에 데이터 정리하는 부분에서 오래걸리는듯 싶음.... 
# from collections import Counter
# def solution4(info, query):
#     answer = []
#     infoList=[]
#     queryScoreList=[]
#     infoScoreList=[]

#     for i in info :
#         lst=i.split(" ")
#         infoList.append(lst)

#     for q in query:
#         qlst= [_ for _ in q.split(' ') if _ != 'and' and _ !='-']
#         for i in infoList:
#             if len(Counter(qlst[:-1])-Counter(i[:-1]))==0:
#                 infoScoreList.append(int(i[-1]))
        
#         target=int(qlst[-1])
#         infoScoreList.sort()
        
#         print("infoScore!!!!!!!!!!!",infoScoreList)
#         print("target",target)

#         if len(infoScoreList)!=0:
#             answer.append( binarySearch(infoScoreList,target))
#         else:
#             answer.append(0)

#         print(answer)
#         infoScoreList.clear()
#     return answer


# #이진검색 
def binarySearch(arr, target):
    print(arr)
    left=0
    right=len(arr)-1
    if arr[left]>target:
        return len(arr)
    if arr[right]<target:
        return 0
    while left < right:
        mid=(left+right)//2
        if arr[mid]<target:
            left=mid+1
        if arr[mid]>=target:
            right=mid
    return len(arr)-left

# print(solution4(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),"result:[1,1,1,1,2,4]")



# #조합을 써야하는거라고 해서 썼더니 효율성 반은 맞았음
# from itertools import combinations
# def solution5(info, query):
#     answer = []
#     infoDict={}

#     for i in info:
#         lst=i.split(" ")
#         infoKey=lst[:-1]
#         infoValue=int(lst[-1])
#         for j in range(5):
#             for k in combinations(infoKey,j):
#                 tmp=''.join(k)
#                 if tmp in infoDict:
#                     infoDict[tmp].append(infoValue)
#                 else:
#                     infoDict[tmp]=[infoValue]

#     for q in query:
#         qlst= q.split(' ')
#         while 'and' in qlst:
#             qlst.remove('and')
#         while '-' in qlst:
#             qlst.remove('-')

#         target=''.join(qlst[:-1])

#         if target in infoDict and len(infoDict[target])!=0:
#             infoDict[target].sort()
#             answer.append(binarySearch(infoDict[target], int(qlst[-1]) ) )
            
#         else:
#             answer.append(0)

#     return answer


# print(solution5(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),"result:[1,1,1,1,2,4]")



#sort가 안에서 돌아가고있어서 오래걸렸던거였네..
from itertools import combinations
def solution6(info, query):
    answer = []
    infoDict={}

    for i in info:
        lst=i.split(" ")
        infoKey=lst[:-1]
        infoValue=int(lst[-1])
        for j in range(5):
            for k in combinations(infoKey,j):
                tmp=''.join(k)
                if tmp in infoDict:
                    infoDict[tmp].append(infoValue)
                else:
                    infoDict[tmp]=[infoValue]
    print(infoDict)
    #이게 문제였음
    for i in infoDict.keys():
        infoDict[i].sort()
        
    for q in query:
        qlst= q.split(' ')
        while 'and' in qlst:
            qlst.remove('and')
        while '-' in qlst:
            qlst.remove('-')

        target=''.join(qlst[:-1])

        if target in infoDict and len(infoDict[target])!=0:
            answer.append(binarySearch(infoDict[target],int(qlst[-1])))
            
        else:
            answer.append(0)

    return answer


print(solution6(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),"result:[1,1,1,1,2,4]")


# 문제 : 복서 정렬하기
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/85002

# 입력 : 
# 복서 선수들의 몸무게 weights
# 복서 선수들의 전적을 나타내는 head2head

# 출력
# 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다.
# 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
# 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
# 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
# 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
# >> 이 규칙에 맞게 복서 선수들의 번호를 다음과 같은 순서로 정렬


# def solution1(weights, head2head):
#     answer=[]
#     # winList=[dict() for i in range(len(weights))] # 싸워서 이긴 번호를 담음
#     # loseList=[dict() for i in range(len(weights))] # 싸워서 진 번호를 담음

#     winList={} # 싸워서 이긴 번호를 담음
#     loseList={} # 싸워서 진 번호를 담음


#     for vs in range(len(head2head)):
#         for i in range(len(head2head[vs])):
#             if head2head[vs][i]=='W':
#                 if vs+1 not in winList:
#                     winList[vs+1] = [i+1]
#                 else:
#                     winList[vs+1].append(i+1)
                    
#             elif head2head[vs][i]=='L':
#                 if vs+1 not in loseList:
#                     loseList[vs+1] = [i+1]
#                 else:
#                     loseList[vs+1].append(i+1)

#     print('winList : ',winList,' loseList:',loseList)


#     winningRate={} # 승률
#     for i,lst in enumerate( zip(winList.items(),loseList.items())):
#         winningRate[i+1]=(len(lst[0][1])/(len(lst[0][1])+len(lst[1][1]))) 
#     print('winningRate : ',winningRate)

#     fatWinning={} # 자기보다 무거운 사람 이긴 횟수
#     cnt=0
#     for index,lst in enumerate(winList):
#         for w in winList[index+1]:
#             if weights[w-1] > weights[index]:
#                 cnt+=1
#         fatWinning[index+1]=cnt
#         cnt=0
#     print('fatWinning : ',fatWinning)

#     sortedWinRate = sorted(winningRate.items(), key=lambda x: x[1], reverse=True)
#     sortedFatWin =sorted(fatWinning.items(), key=lambda x: x[1], reverse=True)
#     print(sortedWinRate,sortedFatWin)

#     temp={}
#     temp2={}
#     cnt=0
#     while winningRate:
#         if not temp:
#             for k,v in winningRate.items():
#                 if v == max(winningRate.values()):
#                     temp[k]=fatWinning[k]
#                     temp = {key : value for key, value in temp.items() if key == k}
#         if len(temp)>0:    
#             for k,v in temp.items():
#                 if v == max(temp.values()):                   
#                     temp2[k]=weights[k-1]
#                     temp2 = {key : value for key, value in temp2.items() if key == k}
#             if len(temp2)>1:
#             elif len(temp2)==0:
#                 answer.append(temp2)
#             print('t2',temp2)
#             temp2 = {key : value for key, value in temp2.items() if key == k}
#         cnt+=1  
#         if cnt==10:
#             break
        
#     return answer

def solution(weights, head2head):
    info = []
    w = len(weights)
    for p in range(w):
        high = [i for i in range(w) if weights[i]>weights[p]] # 더 무거운 사람 인덱스
        over = len([info for info in high if head2head[p][info]=="W"]) # 더 무거운 사람 이긴 수
        rate = 0 if not (w-head2head[p].count("N")) else head2head[p].count("W")/(w-head2head[p].count("N"))
        info.append((p, weights[p], rate, over)) # 번호, 자기무게, 승률, 무거운복서 이긴 횟수
    info = sorted(info, key=lambda x: (x[2], x[3], x[1], -x[0]), reverse=True)
    print(info)
    return [num[0]+1 for num in info]

print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]	),'result : [3,4,1,2]')
# print(solution([145,92,86],	["NLW","WNL","LWN"]),'result : [2,3,1]')
# print(solution([60,70,60],	["NNN","NNN","NNN"]),'result : [2,1,3]')
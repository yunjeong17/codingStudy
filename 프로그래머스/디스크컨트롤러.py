# 문제 : 디스크컨트롤러
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42627

# import heapq

# def solution(jobs):
#     answer = []
#     now, cnt=0, 0
#     heap=[]
#     ok=[]
#     jobs.sort()
#     endtime=[]
#     length=len(jobs)
#     while jobs:
#         # 처음시작 0 > 대기시간 0인것들 heapq에 넣음
#         for job in jobs[:]:
#             if job[0]<=now:
#                 heapq.heappush(heap,job[1])
#                 jobs.remove(job)
#                 ok.append(job)
#         while heap:
#             t=heapq.heappop(heap)
#             for i in ok:
#                 if t==i[1]:
#                     now=i[0]
#                     ok.remove(i)
#                     break
#             if endtime and now > endtime[-1]:
#                 answer.append(t)
#                 endtime.append(t+now)
#             else:
#                 answer.append(endtime[-1]+t-now if answer else t+now)
#                 endtime.append(t+endtime[-1] if endtime else t+now)
            
#             now=answer[-1]
#         else:
#             now+=1
#         print(answer)
#     return sum(answer)//length


# 힙에 리스트를 넣어도 제대로 뽑아준다는 걸 몰랐어서... 위에처럼 해서 틀렸는데
# 새로운걸 알게됨
# 접근법은 완전 비슷했다!!! 나중에 다시 풀면 안보고 풀수있을거같음

import heapq

def solution(jobs):
    answer = 0 
    end, i = 0, 0  #end는 스케쥴 끝난 시점,i는 몇개의 스케쥴이 끝났는지 세는 수
    start = -1  #start는 스케쥴 시작 시점
    hq = [] 
    while len(jobs)>i:  # 스케쥴 끝낸 수가 jobs의 길이 즉, 스케쥴의 개수보다 작다면 (i는 0부터 시작하므로 같다는 빠져야함)
        for job in jobs: # job[0]:요청시점 / job[1]:작업하는데 걸리는 시간 
            if start<job[0]<=end: #시작시간과 끝나는 시간 사이에 스케쥴이 있으면 >> 이렇게하면 굳이나 jobs에서 remove를 할 필요가 없구나.
                heapq.heappush(hq, (job[1], job[0]))  #heap에 푸시해준다.

        if hq: # hq에 뭔가 들어있으면
            now = heapq.heappop(hq) #heap에서 꺼내서 작업을 수행(제일 작은걸 뽑아줌)
            start = end #하나의 작업이 끝났으니 시작시간은 끝나는시간
            end += now[0] #now[0]: 작업하는데 걸리는 시간 / now[1]: 요청시점
            answer += (end-now[1]) # 끝나는시간-요청시점 => 작업의 요청부터 종료까지 걸린 시간
            i += 1 # 한개으 스케쥴을 작업했으니 +1해준다. 
        else: 
            end+=1 # hq에 데이터가 없으면 end를 늘려서 요청시점을 확인할 범위를 늘려줌
    answer = answer//len(jobs) 
    return answer


# print(solution([[0, 3], [4, 3], [8, 3]] ),'reesult: 3')
# print(solution([[0, 5], [6, 1], [6, 2]]),'reesult: 3')
# print(solution([[0, 3], [1, 9], [2, 6]]),'reesult: 9')
# print(solution([[0, 5], [6, 2], [6, 1]] ),'reesult: 3')
# print(solution([[0, 5], [2, 2], [5, 3]]),'reesult: 5')
# print(solution([[0, 10], [4, 10], [15, 2], [5, 11]] ),'reesult:   15')
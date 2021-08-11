# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    cnt=0
    while(len(progresses)>0):
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        if(progresses[0]>=100):
            while(len(progresses)>0 and progresses[0]>=100):
                progresses.pop(0)
                speeds.pop(0) #progresses만 pop할게 아니라 speeds도 같이 pop해줘야함!!
                cnt+=1
            answer.append(cnt)
            cnt=0

    return answer



print(solution([0,0,0,0], [100,50,34,25]),"  result: [1,1,1,1]")

# print(solution([99, 99, 99] ,[1, 1,1]),"  result: [3]")
# print(solution([93, 30, 55],[1, 30, 5]),"  result: [2, 1]")
# print(solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]),"  result:  [3, 3]")
# print(solution([5, 5, 5], [21, 25, 20]),"  result:  [ 3]")
# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]),"  result: [1, 3, 2]")



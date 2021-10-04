# 문제 : 입국심사
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/43238

# * [처리할수 있는 사람수]가 [처리해야되는 사람수]보다 많으면 시간을 너무 여유있게 잡았음 -> 시간을 줄여봄
# * [처리할수 있는 사람수]가 [처리해야되는 사람수]보다 적으면 시간을 너무 빡빡하게 잡았음 -> 시간을 늘려봄

# 다른 사람 풀이 >> 시간 지나서 다음에 한번 더 풀어보기 
def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n #가장 비효율적으로 심사했을 때 걸리는 시간
    while left <= right:
        mid = (left+ right) // 2 #모든 심사관들에게 주어진 시간. 
        people = 0 #모든 심사관들이 mid분 동안 심사한 사람의 수
        for time in times:
            people += mid // time
            print('p:',people,'    mid:',mid,'  time:', time,times)
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 break
            if people >= n:
                print('break')
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
            print('mid1',mid,answer,right,left)
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1
            print('mid2',mid,answer,right,left)
    return answer



# n: 대기 명수 - 6  
# times: 각 심사대에서 심사에 걸리는 시간 - [7,10]
print(solution(6, [7, 10]),'result:28')

# print(solution(3, [1, 1, 1] ),'result:1')
# print(solution(3, [1, 2, 3]),'result:2')

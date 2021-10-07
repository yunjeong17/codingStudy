# 문제 : 체육복
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42862

# 입력 : 
# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve

#출력 : 체육수업을 들을 수 있는 학생의 최댓값

def solution(n, lost, reserve):
    answer = 0
    status=[True]*n
    # 도난당한 학생이 여벌의 체육복을 가지고있을때 lost와 reserve 리스트에서 없애준다. >> 본인꺼 입고 체육수업을 들을수있어서
    lost2= list(set(lost)-(set(lost)&set(reserve)))
    reserve2=list(set(reserve)-(set(lost)&set(reserve)))
    
    print(lost2,reserve2)

    for i in lost2:
        status[i-1]=False
    # print('status:',status)

    for i in lost2: # 번호는 인덱스보다 +1된 상태
        # print('lost : ',i-1) 
        if (i-1) in reserve2: # i번 학생 앞자리 i-1 >> status 인덱스는 i-2번임 
            reserve2.remove(i-1)
            status[i-1]=True #status[i-1]하면 현재 학생의 status
            # print(reserve,'i-2', (i-2))
        elif i+1 in reserve2: # i번학생 뒷자리 학생 i+1 >> status인덱스는 i
            reserve2.remove(i+1)
            status[i-1]=True
        
        # print('re',reserve,status)
    answer=sum(status)
    return answer

print(solution(5,	[2, 4],	[1, 3, 5]	),'result:5')
# print(solution(5,	[2, 4],	[3]),'result:4')
# print(solution(3,	[3],	[1]),'result:2')
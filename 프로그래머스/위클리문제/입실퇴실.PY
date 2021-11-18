# 문제 : 입실퇴실
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/86048


#회의실에 입실한 순서가 담긴 정수 배열 enter,
#  퇴실한 순서가 담긴 정수 배열 leave
# 각 사람별로 '반드시' 만난 사람은 몇 명인지 번호 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
def solution(enter, leave):
    answer = [0]*len(enter)
    dict={}
    cnt1=0
    cnt2=0
    while True:
        if leave[cnt2] not in dict:
            for i in dict.keys():
                dict[i]+=1
        
            dict[enter[cnt1]]=len(dict)
            cnt1+=1
        else:
            answer[leave[cnt2]-1]=dict[leave[cnt2]]
            del dict[leave[cnt2]]
            cnt2+=1
        if cnt2>=len(leave):
            break
    
    return answer

# print(solution([1,3,2],[1,2,3]),'result: [0,1,1]')
print(solution([1,4,2,3],[2,1,3,4]),'result: [2,2,1,3]')
# print(solution([3,2,1],[2,1,3]),'result: 	[1,1,2]')
# print(solution([3,2,1],[1,3,2]),'result: [2,2,2]')
# print(solution([1,4,2,3],[2,1,4,3]),'result:[2,2,0,2] ')
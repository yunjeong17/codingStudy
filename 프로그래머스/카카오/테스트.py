# 링크 : https://programmers.co.kr/tryouts/3929/challenges?original_test_id=27390&original_token=a53744d8e0e236c80f695e7637afaffa

# 직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다.
#  점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요.
#   단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.

# 제한사항
# v는 세 점의 좌표가 들어있는 2차원 배열입니다.
# v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
# 좌표값은 1 이상 10억 이하의 자연수입니다.
# 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요.

def solution(v):
    answer = [0,0]
    dictX={}
    dictY={}
    for i in v:
        if i[0] not in dictX:
            dictX[i[0]]=1
        else:
            dictX[i[0]]=dictX[i[0]]+1
        
        if i[1] not in dictY:
            dictY[i[1]]=1
        else:
            dictY[i[1]]=dictY[i[1]]+1
        print(dictX,dictY)

    for k,v in dictX.items():
        if v==1:
            answer[0]=k

    for k,v in dictY.items():
        if v==1:
            answer[1]=k
    return answer




def solution2(v):
    answer = [0,0]
    temp=list(zip(*v))
    for i in range(len(v)):
        if temp[0].count(temp[0][i])==1 : 
            answer[0]=temp[0][i]
        if temp[1].count(temp[1][i])==1 : 
            answer[1]=temp[1][i]
    return answer

print(solution2([[1, 4], [3, 4], [3, 10]]),"result: [1, 10]")
print(solution2([[1, 1], [2, 2], [1, 2]]),"result: [2, 1]")
# print(solution(),"result: ")

lst=[[1,2,3],[4,5,6]]
# 크레인 인형뽑기
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    result=[]
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]!=0:
                result.append(board[i][m-1])
                board[i][m-1]=0
                break
        if len(result)>1 and result[-1]==result[-2]:
            result.pop()
            result.pop()
            answer+=2

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]),"result:4")
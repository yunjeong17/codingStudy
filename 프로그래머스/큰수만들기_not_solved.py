# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

   
def solution(number, k):
    answer = ''
    return answer

#와...입출력 예제 빼고 다 틀림 대박,....다시 풀기...
def solution1(number, k):
    answer = ''
    cnt=0
    
    numlst = list(map(int, list(number)))
    firstMax=numlst.index(max(numlst[:k]))
    for i in range(firstMax):
        numlst.pop(0)
        cnt+=1
    num=numlst[0]
    i=0
    while cnt<k:
        if num >= numlst[i]:
            num=numlst[i]
        else :
            num=numlst[i]
            numlst.pop(i-1)
            cnt+=1
        if i == len(numlst)-1:
            i=0
        i+=1
    print(numlst)
    for i in numlst:
        answer+=str(i)
    return answer

print(solution("1924",2),"result: 94")
print(solution("1231234",3),"result: 3234")

# '41'77252841 >> 77'2'52841 >> 775'2'841 >> 775841
print(solution("4177252841",4),"result:775841")
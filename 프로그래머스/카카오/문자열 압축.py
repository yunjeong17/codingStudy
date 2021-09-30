# 문제 : 문자열 압축
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/60057


#같은 숫자는 싫어에서 사용했던 방법 이용 >> 일단 1개 일때만 
def solution(s):
    answer = []
    result=""
    k=0
    cnt=1
    answer.append(["",0])
    for i in range(len(s)):
        if(s[i]!=answer[k][0]):
            answer.append([s[i],1])
            k+=1
            cnt=1
        else:
            cnt+=1
            answer[len(answer)-1][1]+=1        
    for i in answer[1:]:
        if i[1]==1:
            result+=i[0]
        else:
            result+=str(i[1])+i[0]
    return len(result)


# print(solution("aabbaccc"),"result: 7")
# print(solution("ababcdcdababcdcd"),"result: 9")
# print(solution("abcabcdede"),"result: 8")
# print(solution("abcabcabcabcdededededede"),"result: 14")
# print(solution("xababcdcdababcdcd"),"result: 17")



# 2글자씩, 3글자씩, ... 할 때는???
# aabcabc일때 3글자씩하는거면 aab랑 cab랑 비교해서 없으면 abc랑 abc랑 비교하는식..해야하는데,,? 이걸 어떻게 하지?
# 문자열`은  "제일 앞"부터 정해진 길이만큼 잘라야 합니다. << !!!
# s[i:i+j]      [i+j:i+2*j]
#j=1 i=0
#  0:1            0+1:0+2*1 >> 1:2
#j=1 i=1
#  1:2            1+1:1+2*1 >> 2:3

def solution2(s):
    answer = []
    rset=[]
    result=""
    k=0
    cnt=1
    if len(s)==1:
        return 1
    for j in range(1, len(s)//2+1): #4글자면 4//2+1 = 2+1 = 3 전까지 >> 1,2
        answer.append(["",0])
        for i in range(0,len(s),j): #4//1 =4            4//2=2 개수에 맞게 돌아가게
            if(s[i:i+j]!=answer[k][0]):
                answer.append([s[i:i+j],1])
                k+=1
                cnt=1
            else:
                cnt+=1
                answer[len(answer)-1][1]+=1
            print(j,answer)
        
        for i in answer[1:]:
            if i[1]==1:
                result+=i[0]
            else:
                result+=str(i[1])+i[0]
            print(j,result)
        rset.append(len(result))
        print(answer)
        answer=[]
        result=""
        k=0
        cnt=1
        print("======================================")
        print(rset)
    return min(rset)
print(solution2("aabbaccc"),"result: 7")
# print(solution2("ababcdcdababcdcd"),"result: 9")
# print(solution2("abcabcdede"),"result: 8")
# print(solution2("abcabcabcabcdededededede"),"result: 14")
# print(solution2("xababcdcdababcdcd"),"result: 17")
# print(solution2("x"),"result: 1")
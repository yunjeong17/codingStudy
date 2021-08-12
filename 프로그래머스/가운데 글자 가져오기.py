# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    if( int(len(s)%2 ) == 1 ): #홀수일때
        num=int(len(s)/2) +1
        answer=s[num-1]
    else: #짝수일때
        num=int(len(s)/2)
        answer=s[num-1:num+1]
    
    return answer


# 위 풀이 방법과 같지만 좀 더 간결하게 풀어봤다 !! 이제 if문 삼항 표현식도 좀 활용 수 있겠다!!
def solution2(s):
    return s[len(s)//2] if len(s)%2==1 else s[len(s)//2-1:len(s)//2+1]

print(solution2("abcde"))
print(solution2("abqcde"))
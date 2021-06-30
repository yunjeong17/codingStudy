def solution(number, k):
    answer = ''
    numlst = list(map(int, list(number)))
    index=numlst.index(max(numlst))
    
    return answer

print(solution("1924",2))
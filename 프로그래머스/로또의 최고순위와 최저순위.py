def solution(lottos, win_nums):
    min=0
    max=0
    answer=[]
    dic={0:6,1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    for number in lottos:
        if number in win_nums :
            min+=1
            max+=1
        if number==0:
            max+=1

    answer.append(dic.get(max)) 
    answer.append(dic.get(min)) 
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]),"    result:[3, 5]")
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]),"    result:[1, 6]")
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]),"    result:[1, 1]")


#다른사람 풀이
def solution2(lottos, win_nums):
    rank={0:6,1:6, 2:5, 3:4, 4:3, 5:2, 6:1} #딕셔너리 선언한건 나랑 같음
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]] #set 사용
    # 구매한 로또번호를 set해서 중복제거(중복은 0밖에 없음)
    # 최저 등수는 거기에 당첨번호를 set해서 형 같게 해주고 둘이 같은거 있는 길이를 반환  > 그 길이는 0을 제외한 맞춘 숫자의 개수가 됨
    # 최고 등수는 거기에 lottos.count(0)을 더해줌. 여기서 lottos.count(0)란? 0의 개수를 세서 그 값을 반환해주는 것.
print(solution2([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]),"    result:[3, 5]")
print(solution2([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]),"    result:[1, 6]")
print(solution2([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]),"    result:[1, 1]")
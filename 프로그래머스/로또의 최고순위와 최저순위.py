# 로또의 최고순위와 최저순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

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

# print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]),"    result:[3, 5]")
# print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]),"    result:[1, 6]")
# print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]),"    result:[1, 1]")

#다른사람 풀이
def solution2(lottos, win_nums):
    rank={0:6,1:6, 2:5, 3:4, 4:3, 5:2, 6:1} #딕셔너리 선언한건 나랑 같음
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]] #set 사용
    # 딕셔너리로 등수를 체크해준 것은 나랑 같다. 그런데 이사람은 set(집합)을 써서 &(교집합)를 할 수 있게했다. 
    # &를 해서 true의 개수(맞은 개수)를 최저순위에 넣어주고, 최고순위는 앞서 구한거에 lottos에 있는 0의 개수를 세서 더해줬다. 
print(solution2([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]),"    result:[3, 5]")
print(solution2([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]),"    result:[1, 6]")
print(solution2([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]),"    result:[1, 1]")
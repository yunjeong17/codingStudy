# 문제 : 베스트앨범
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42579

# genres: 고유번호 i인 노래의 장르
# plays : 고유번호 i인 노래의 재생횟수

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
def solution(genres, plays):
    answer = []
    dic={}
    totalPlays={}
    for i,(g,p) in enumerate (zip(genres,plays)):
        if g in dic:
            dic[g].append([i,p])
            totalPlays[g]+=p
        else:
            dic[g]=[[i,p]]
            totalPlays[g]=p

    totalPlaysTuple=sorted(totalPlays.items(), key=lambda x: -x[1])
    print(totalPlaysTuple)
    # 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    order1=[]
    for i in totalPlaysTuple:
        order1.append(i[0])

    # 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    for d in order1:
        temp=sorted(dic[d], key=lambda x:-x[1])
        print(temp)
        if len(temp)>=2:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])

    print(dic,totalPlaysTuple,order1,answer)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]),"result:[4, 1, 3, 0]")
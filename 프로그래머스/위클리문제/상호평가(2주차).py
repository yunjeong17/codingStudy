# 문제 : 상호 평가
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/83201

#자신이 자신에게 준 점수가 유일한 최고점 최저점이면 제외하고 평균내기

def solution(scores):
    grade={'A':[90,100],'B':[80,89],'C':[70,79],'D':[50,69],'F':[-1,49]}
    answer = ''
    cnt=0
    for i in range(len(scores)):
        mine=scores[i][i]
        if not(mine > min(scores[i]) and mine < max(scores[i])):
            scores[i][i]=-1
    print(scores)
    for i in range(len(scores)):
        point = list(list(zip(*scores))[i])
        if point[i]==-1:
            point.remove(-1)
        print(point)
        avgPoint=sum(point)/(len(point))
        for key,value in grade.items():
            if avgPoint >= value[0] and avgPoint <= value[1] :
                answer+=key
    return answer


def solution2(scores):
    grade={'A':[90,101],'B':[80,90],'C':[70,80],'D':[50,70],'F':[0,50]}
    answer = ''

    newScores = list(map(list,zip(*scores)))
    for i in range(len(newScores)):
        mine=newScores[i][i]
        # print(mine, mine >= min(newScores[i]),mine <= max(newScores[i]) ,min(newScores[i]),max(newScores[i]),(mine >= min(newScores[i]) and mine <= max(newScores[i])) )

        # 해당 범위안에 내가 준 점수가 있는것이 아니면
        if not(mine > min(newScores[i]) and mine < max(newScores[i])):
            del newScores[i][i]
    for i in newScores:
        avg=sum(i)/len(i)
        for key, value in grade.items():
            if avg >= value[0] and avg < value[1] :
                answer+=key
    return answer

def solution3(scores):
    grade={'A':[90,100],'B':[80,89],'C':[70,79],'D':[50,69],'F':[0,49]}
    answer = ''
    newScores = list(map(list,zip(*scores)))

    for i in range(len(newScores)):
        mine=newScores[i].pop(i)
        print(newScores,"  mine:",mine,"   min:", min(newScores[i]),"   max:", max(newScores[i]))

        if (mine >=  min(newScores[i]) and mine <= max(newScores[i]) ):
            newScores[i].append(mine)
            print('i:',i,'scores',newScores[i])

    #너저분해!!!!!!!!!!
    for i in newScores:
        avg=sum(i)/len(i)
        print(avg,i)
        if avg >= 90:
            answer+="A"
        elif avg >=80:
            answer+="B"
        elif avg >=70:
            answer+="C"
        elif avg >= 50:
            answer+="D"
        else:
            answer+="F"
    return answer


solution4 = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))

# print(solution2([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]),"  FBABD")
# print(solution2([[50,90],[50,87]]),"  DA")
# print(solution2([[100,20,20],[40,40,20],[10,20,100]]),"FFF")
# print(solution2([[75, 50, 100], [75, 100, 20], [100, 100, 20]]),'result: BBF')
# print(solution2([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),'result: FFFF')
# print(solution4([[70,49,90],[68,50,38],[73,31,100]]))
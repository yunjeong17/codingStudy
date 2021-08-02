# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

# 조건
# 2명을 초과할 수 없다
# limit 무게를 초과할 수 없다

#효율성 0점... 정확도는 다 맞는데..
def solution1(people, limit):
    boat=[]
    people.sort(reverse=True) #내림차순으로 sort
    while people: # people이 빌떄까지 
        p1=people.pop(0) #
        if len(people)==0: #people이 비었으면
            boat.append([p1]) #이번에 pop해둔 p1을 보트에 넣고 while문 종료
            break
        if p1 + people[-1]>limit: #pop해둔 p1과 people의 맨 마지막인덱스(가장 작은수)의 힙이 limit보다 크면
            boat.append([p1]) #p1만 append해서 태워보냄 (제일큰수가 제일 작은수랑 같이 탈수없으면 무조건 혼자타야하므로 혼자 보냄)
        elif p1 + people[-1]<=limit: # limit보다 작으면
            p2=people.pop() #같이 태워보내기위해 맨마지막 사람을 pop해서
            boat.append([p1,p2]) #맨앞과 맨뒤를 같이 태워보냄
    return len(boat)

# pop 없이 하기
# 다른 사람 코드 참고했음
# 로직은 동일함
def solution2(people, limit):
    answer=0
    l=0
    r=len(people)-1
    people.sort(reverse=True) #내림차순으로 sort
    while l < r :
        if people[l] + people[r]>limit: #맨앞과 맨뒤의 힙이 limit보다 크면
            l+=1 #맨 앞만 넣고 보트 보냄
        else : # limit보다 작으면 맨앞 맨뒤 한 보트에 태워서 보냄
            l+=1 
            r-=1
        answer+=1
    if l==r: #마지막에 한명 남았을 때
        answer+=1 #한명도 태워서 보냄

    return answer


print(solution1([70, 50, 80, 50],100),"reulst: 3")
print(solution1([70, 80, 50],100),"reulst: 3")
print(solution1([40, 50, 60, 90] ,100),"reulst: 3")
print(solution1([10,20,30,40,50,60,70,80,90], 100),"reulst: 5")

print("==============================================================")

print(solution2([70, 50, 80, 50],100),"reulst: 3")
print(solution2([70, 80, 50],100),"reulst: 3")
print(solution2([40, 50, 60, 90] ,100),"reulst: 3")
print(solution2([10,20,30,40,50,60,70,80,90], 100),"reulst: 5")

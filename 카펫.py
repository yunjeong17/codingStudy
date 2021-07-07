# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842


#넓이로 풀었음!
# yellow가 안쪽 brown이 바깥쪽
# 한칸의 길이는 1로 생각 > 즉 한칸은 넓이가 1임
# yellow는 brown으로 둘러싸여있으니까 (yellow의 가로길이+brown(2) = 전체 가로길이 )*(yellow의 세로길이 + brown(2) = 전체 세로 길이) = yellow넓이+brown넓이
# 전체 넓이 >> 전체 넓이 - yellow의 넓이 = brown의 넓이
def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):     
        if(yellow%i!=0): # yellow를 i로 나눴을때 정수가 아니면 카펫모양을 절대 만들 수 없기때문에 아래를 진행하지않고 다음 i로 넘어감
            continue

        yellow2=yellow//i # yellow는 yellow의 넓이 i는 한 변이라고 생각함.
        if (( (yellow2+2)*(i+2) )-yellow) == brown: 
            #yellow는 brown으로 둘러싸여있으니까 (yellow의 가로길이+brown(2) = 전체 가로길이 )*(yellow의 세로길이 + brown(2) = 전체 세로 길이) - yellow넓이 = brown넓이
            answer=[yellow2+2,i+2]
            answer.sort(reverse=True)
            break;
    return answer

# □ □ □ □ 1
# □ ■ ■ □ 2
# □ □ □ □ 3
print(solution(10,2),"result: [4, 3]")
print("==============================")
# # □ □ □ 1
# # □ ■ □ 2
# # □ □ □ 3
print(solution(8,1),"result: [3, 3]")
print("==============================")

# # □ □ □ □ □ □ □ □ 1
# # □ ■ ■ ■ ■ ■ ■ □ 2
# # □ ■ ■ ■ ■ ■ ■ □ 3
# # □ ■ ■ ■ ■ ■ ■ □ 4
# # □ ■ ■ ■ ■ ■ ■ □ 5
# # □ □ □ □ □ □ □ □ 6
print(solution(24,24),"result: [8, 6]")
print("==============================")
# # □ □ □ □ □ 1
# # □ ■ ■ ■ □ 2
# # □ ■ ■ ■ □ 3
# # □ □ □ □ □ 4
print(solution(12,4),"result: [4, 4]")
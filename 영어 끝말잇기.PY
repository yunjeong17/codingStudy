# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3

#간결하게 풀기위해 노력해야함

#내 풀이
def solution(n, words):
    answer = []
    result=[0,0]
    user=0
    turn=0
    cnt=0
    for w in words :
        if(user%n == 0): #ex: 3명이서 할떄 (user0,user1,user2)가 있으면 user2%total2==0이므로 다시 첫사람에게 돌아감
            turn+=1 #한바퀴 돌면 턴수 올려줌
            user=0  #유저는 처음 사람부터 다시
        if(len(answer)==0 ):
            answer.append(w)
        else :
            if( w not in answer and answer[cnt-1][-1] == w[0] ): #끝말잇기 리스트에 없고, 저장된 단어의 마지막 알파벳과 현재 들어온 단어의 첫 알파벳이 같으면 끝말잇기리스트에 추가 
                answer.append(w)
            else : #있으면 실패
                result=[user+1,turn]
                break
        user+=1
        cnt+=1
    return result


#다른사람 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]),'result:[0,0]')
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]),'result:[3,3]' )
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]),'result:[1,3]' )



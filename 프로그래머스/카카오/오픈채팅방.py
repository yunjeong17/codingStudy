# 문제 : 오픈 채팅방
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    user={}
    for r in record:
        row=r.split()
        if row[0]=="Enter" or row[0]=="Change":
            user[row[1]]=row[2]

    for r in record:
        row=r.split()
        if row[0]=='Enter':
            s= user[row[1]]+'님이 들어왔습니다.'
            answer.append(s)
        if row[0]=='Leave':
            s = user[row[1]]+"님이 나갔습니다."
            answer.append(s)
    return answer



# 다른 사람 풀이
# 프린터가 있는것도 좋았고, 체인지가 아닐 때만 로그를 append 하는 것도 훨 더 깔끔하고 중복되는 코드가 없어서 좋다. 
def solution2(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]),'result:["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]')
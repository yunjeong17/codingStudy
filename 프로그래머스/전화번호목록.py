# 전화번호목록
# https://programmers.co.kr/learn/courses/30/lessons/42577


#효율성 0점
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if phone_book[i]==j[:len(phone_book[i])]:
                return False
    return True


#효율성테스트 3,4번에서 걸림
def solution2(phone_book):
    phone_book.sort()
    first=""
    print(phone_book)
    for i in range(0,len(phone_book)):
        for j in phone_book[i+1:]:
            # print(first,"        ",phone_book[i],"   ",j)
            if j.startswith(phone_book[i]):
                return False
            if first!=phone_book[i][0]:
                first=phone_book[i][0]
                break

    return True


#정확도 ㅇㅋ 효율성 ㅇㅋ 근데 해시를 안썼음... 해시 쓰는 방법 찾아보기
def solution3(phone_book):
    phone_book.sort()
    first=""
    print(phone_book)
    for i in range(0,len(phone_book)-1):
        if(phone_book[i]==phone_book[i+1][:len(phone_book[i])]):
            return False
    return True

#다른사람 풀이 찾아보기 (아직 딱히 더 효율적인걸 못찾음 ㅠ)
def solution(phoneBook):
    return 0


print(solution3(["1234", "1235", "567"])," result:true ")
print(solution3(["119", "97674223", "1195524421"])," result:false ")
print(solution3(["123","456","789"]	)," result:true")
print(solution3(["12","123","1235","567","88"])," result:false ")
print(solution3(["12567","555123","1444235","75567","6688","33555","555"])," result:False")
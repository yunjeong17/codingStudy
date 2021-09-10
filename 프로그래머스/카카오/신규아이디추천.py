# 문제 : 신규아이디 추천
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/72410

#제한 사항
#new_id는 길이 1 이상 1,000 이하인 문자열입니다.
#new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
#new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.


def solution(new_id):
    answer = ''
    
    #1단계 :모든 대문자를 대응되는 소문자로 치환
    new_id=new_id.lower()
    print('step1 :',new_id)

    #2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for i in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id=new_id.replace(i,"")
    print('step2 :',new_id)


    #3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    temp=""
    i=0
    while(len(new_id)>=i+1 ):
        if temp=='.' and new_id[i]=='.':
            new_id=new_id[0:i]+new_id[i+1:]
            i-=1
        temp=new_id[i]
        i+=1
    print('step3 :',new_id)


    #4단계 : 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id[-1]=='.':
        new_id=new_id[:-1]
    if len(new_id)>0 and new_id[0]=='.':
        new_id=new_id[1:]
    print('step4 :',new_id)


    #5단계 : 빈 문자열이라면, new_id에 "a"를 대입    
    if len(new_id)==0:
        new_id='a'
    print('step5 :',new_id)


    #6단계 : 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #        만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    new_id=new_id[:15]
    if new_id[-1]=='.':
        new_id=new_id[:-1]
    print('step6 :',new_id)


    #7단계 : new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    # print('step7 :',new_id)
    if len(new_id)<3:
        while len(new_id)<3:
           new_id+=new_id[-1]
   
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"),"result:	bat.y.abcdefghi")
print(solution("z-+.^."),"result : z--")
print(solution("=.="),"result : aaa")
print(solution(	"123_.def"),"result: 123_.def")
print(solution("abcdefghijklmn.p"),"result: abcdefghijklmn")
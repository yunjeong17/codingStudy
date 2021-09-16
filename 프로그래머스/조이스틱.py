# 문제 : 조이스틱 
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42860


# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 // 맨 마지막위치에서 오른쪽 못감.



# 근본적으로 문제가 있는 코드... 다시 풀어보자 ㅎㅎ
# def solution(name):
#     answer = 0
#     cursor=0
#     result="A"*len(name)
#     alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','F','W','X','Y','Z']

#     while result!=name:
#         print(cursor)
#         print("--------------------------------------")
#         if result[cursor]!=name[cursor]: #name과 result의 현재 커서의 위치의 값이 같지 않으면
#             # EX) 커서: 0 ,result="AAA", name="JAN"이면 A와 J가 같지 않기때문에 같게 만들어줘야함  
#                 result=str(result[:cursor]+ name[cursor]+result[cursor+1:])
#                 answer+=abs(alphabet.index(name[cursor])-alphabet.index(result[cursor]))
#                 print(cursor,result,name,answer)
#                 break
                
#                 print()
#         else: #값이 서로 같으면 커서를 다른 위치로 옮겨줘야함
#             for i in range(1,len(name)):
#                 c1=-1
#                 c2=-2
#                 if name[cursor+i] !='A':
#                     if cursor+i>len(name)-1:
#                         c1= cursor-len(name)
#                         print(cursor,c1,"c1")
#                     else:
#                         c1=cursor+i
#                     print(cursor,c1,"c1")
#                 elif name[cursor-i]!='A':
#                     if cursor-i<0:
#                         c2=cursor+(len(name)-i)
#                     else: 
#                         c2=cursor-i
#                     print(cursor,c2,"c2")

#                 if (c1==c2) or ((c1!=-1 or c2!=-2) and abs(cursor-c1)<=abs(cursor-c2)):
#                     print(answer,cursor,c1,'c1')
#                     answer+=abs(cursor-c1)
#                     cursor=c1
#                     print(cursor,c1,"c1")
#                     c1=-1
#                     break
#                 elif ((c1!=-1 or c2!=-2) and abs(cursor-c1)>abs(cursor-c2)):
#                     print(answer,cursor,c2,'c2')
#                     answer+=abs(cursor-c2)   
#                     cursor=c2
#                     print(cursor,c2,"c2")
#                     c2=-1
#                     break  
#                 print(name,result,cursor)
#     return answer



# 다른사람꺼 참고해서 함
def solution2(name):
    answer = 0
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','F','W','X','Y','Z']

    
    minMove=len(name)-1 # 최대로 많이 움직일때 (왼쪽부터 오른쪽끝까지 갔을때)를 저장
    for i,n in enumerate(name):
        if i!='A':#위아래 변경부터 계산 전부하기
            answer += (len(alphabet)-alphabet.index(n)) if alphabet.index(n)>len(alphabet)//2 else alphabet.index(n)

            #양옆 변경 계산
        next=i+1
        while next<len(name) and name[next]=='A':
            next+=1 
                # name에서 i이후로 a가 아닌걸 만날때까지 next를 키움
                # BBAABB가 있을때 0번째 FOR문에서는 next=1 name[1]은 A가 아니므로 while을 돌지않음
                #오른쪽으로 갔다가(i) 원래자리로 돌아갔다가(i) 뒤에서부터 처음에 A끝을 알아둔곳(next)까지 더함
        minMove = min(minMove, i + i + len(name) - next)
        #위의 걸 수행한거중 가장 작은걸 저장해둠
    answer += minMove
    print(answer)


    return answer


print(solution2("JEROEN"),'result: 	56')
print(solution2("JAN"),'result: 	23')

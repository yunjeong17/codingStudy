# 문제 : 직업군 추천하기
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/84325
import operator
def solution(table, languages, preference):
    dict={} #table을 정리한 딕셔너리 :: dict >> key=회사이름 value={key:언어이름 , value: 점수}
    temp={} # 선호언어 호감도와 점수를 곱해서 값을 넣은 것  :: temp >> >> key=회사이름 value={key:선호 언어 이름 , value: 호감도*점수} 
    temp2={} #temp를 정리해서 회사별 점수 총합을 담은 딕셔너리

    for t in table:
        row=t.split(" ")
        r=row[1:]
        r.reverse()
        dict[ row[0] ]={v:i+1 for i,v in enumerate(r)}
        temp[ row[0] ]={}

    
    print('dict',dict)
    print('temp',temp)
    print("=============")
    for k,v in dict.items():
        for l,p in zip(languages,preference):
            temp[k][l]=dict[k][l]*p if l in dict[k] else 0
           # print('dict k=',k ,' l = ',l,' 해당 점수=',dict[k][l] if l in dict[k] else 0, '호감도',p,' 곱했음:',dict[k][l]*p if l in dict[k] else 0 )
            # print('temp::::',temp)
        print('===============')
    
    for k,v in temp.items():
        temp2[k]=sum([v for v in temp[k].values()])

    return max(sorted(temp2.items()), key=operator.itemgetter(1))[0]



#프린트문 뺀 제출용
def solution2(table, languages, preference):
    temp={}
    dict={}
    temp2={}
    for t in table:
        row=t.split(" ")
        r=row[1:]
        r.reverse()
        dict[ row[0] ]={v:i+1 for i,v in enumerate(r)}
        temp[ row[0] ]={}

    for k,v in dict.items():
        for l,p in zip(languages,preference):
            temp[k][l]=dict[k][l]*p if l in dict[k] else 0

    
    for k,v in temp.items():
        temp2[k]=sum([v for v in temp[k].values()])
    return max(sorted(temp2.items()), key=operator.itemgetter(1))[0]

print(solution2(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5]),"result: HARDWARE")
# print(solution2(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"],	[7, 5]),'result: "PORTAL"')
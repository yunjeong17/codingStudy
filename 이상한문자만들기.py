#이상한 문자 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930

#enumerate
#반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
#인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
#(인덱스번호, 원소)형식으로 출력

def solution(s):
    answer = ''
    cnt=0
    c=0
    for i in s:
        if(i!=" "):
            if (int(cnt%2)==0):
                i=i.upper()
            else:
                i=i.lower()     
            s=s[:c]+i+s[c+1:]
            cnt+=1    
        else:
            cnt=0
        c+=1
    answer=s
    return answer



def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ") ) )

#map(함수,[리스트]) 반복해서 수행해줌
#join([리스트]) 공백없이 문자열 붙여줌
#print(solution("   As asdf d df  d  "))
print(toWeirdCase("asdf ASDDD FdSSF  df  "))
# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

# 다시풀자 ㅎㅎㅎ.....
import numpy 
def solution(arr1, arr2):
    answer = [[]]
    tmp=[]
    arr3=[]
    temp=0

    if len(arr1[0])!=len(arr2):
        t=arr1
        arr1=arr2
        arr2=t
    arr3=list(map(list,zip(*arr2)))
    print(arr3)
    for i in range(len(arr1)):

        for j in range(len(arr3)):
            for a,b in zip(arr1[i],arr3[j]):
                temp=(a*b)+temp
            tmp.append(temp)
            temp=0
    # print(len(arr3),len(arr3[0]),,len(arr1[0]))
    # answer = numpy.reshape(tmp,(len(arr3),len(arr1[0])))
    answer = numpy.reshape(tmp,(len(arr1),len(arr3[0]))) #reshape(lst, 행의 개수,열의 개수 ) list[열][행]
    for i in range(len(answer)):
        answer[i]=answer[i].tolist()
    answer = answer.tolist()
    return answer


print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]),"result : [[15, 15], [15, 15], [15, 15]]")
print(solution( [[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4], [2, 4], [3, 1]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],  [ [5, 4, 3], [2, 4, 1], [3, 1, 1] ]   ),"result : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]")
# print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]]),"")
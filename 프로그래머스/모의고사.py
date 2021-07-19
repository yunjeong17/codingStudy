#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    a = [1, 2, 3, 4, 5]*2000
    b = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

    cnt=0
    aa=0
    bb=0
    cc=0
    for i in answers:
        if a[cnt]==i:
            aa+=1
        if b[cnt]==i:
            bb+=1
        if c[cnt]==i:
            cc+=1
        cnt+=1
    result={'1':aa,'2':bb,'3':cc}
    result_list=[]
    max_v = result[max(result, key=lambda k: result[k])]

    for key, value in result.items():
        if value == max_v:
            result_list.append(int(key))
    return result_list
print(solution([1,3,2,4,2]))
# def stu1(answers):
#     k=1
#     a=[]
#     #1번째 학생
#     for i in range(1,len(answers)+1):
#         a.append(k)
#         if k>4:
#             k=1
#         else:
#             k+=1
        
            
#     return a

# def stu2(answers):
#     #2번째 학생
#     b=[]
#     b.append(2)
#     k=1
#     for i in range(1,len(answers)):
#         if(b[i-1]==2):
#             if k<6:
#                 b.append(k)
#                 k+=1
#                 if k==2:
#                     k+=1
#             elif k>5:
#                 k=1
#                 b.append(k)
#                 k+=2
#         if(b[i-1]!=2):
#             b.append(2)
#     return b

# def stu3(answers):
#         #3번째 학생
#     k=1
#     c=[]
#     c.append(1)
#     for i in range(1,len(answers)):
#         if c[i-1]==k :
#             c.append(k)
#             k+=1
#         elif c[i-1]!=k:
#             c.append(k)   
#     return c
# def solution(answers):
#     answer = []
#     a=[]
#     b=[]
#     c=[]

#     a=stu1(answers)
#     b=stu2(answers)
#     c=stu3(answers)

#     cnt=0
#     aa=0
#     bb=0
#     cc=0
#     for i in answers:
#         if a[cnt]==i:
#             aa+=1
#         if b[cnt]==i:
#             bb+=1
#         if c[cnt]==i:
#             cc+=1
#         cnt+=1
#     result={'1':aa,'2':bb,'3':cc}
#     result_list=[]
#     max_v = result[max(result, key=lambda k: result[k])]

#     for key, value in result.items():
#         if value == max_v:
#             result_list.append(int(key))
#     return result_list

# asr=[2,2,3,2,2]


# print(solution(asr))
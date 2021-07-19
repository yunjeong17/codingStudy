#https://programmers.co.kr/learn/courses/30/lessons/67256
#키패드 누르기
#1,4,7 누를때 왼손
#3,6,9 누를때 오른손
def solution(numbers, hand):
    answer = ''
    keypad=[[1,2,3],[4,5,6],[7,8,9],[74,0,67]]
    lSelect_row,lSelect_column=3,0 #왼손 현재 위치
    rSelect_row,rSelect_column,=3,2 #오른손 현재 위치
    lr=''
    row=0
    lst=[]
    for num in numbers:
        if num>=1 and num<=3 :
            row=0
        elif num>=4 and num<=6:
            row=1
        elif num>=7 and num<=9:
            row=2
        else:
            row=3
        column=keypad[row].index(num)
        print("key:",keypad[row][column])
        if column==0: #왼쪽줄
            lr="L"
            lSelect_column=column
            lSelect_row=row
        elif column==2: #오른쪽줄
            lr="R"
            rSelect_column=column
            rSelect_row=row
        else: #가운데줄
            lsum=abs(lSelect_column-column)+abs(lSelect_row-row) #왼손 거리
            rsum=abs(rSelect_column-column)+abs(rSelect_row-row) #오른손 거리
            if lsum>rsum: #오른손이 더 가까울때
                rSelect_column=column
                rSelect_row=row
                lr="R"
            elif lsum<rsum: #왼손이 더 가까울때
                lSelect_column=column
                lSelect_row=row
                lr="L"
            else: #거리가 같을때 왼손잡이 오른손잡이로 결정
                if(hand=="right"):
                    rSelect_column=column
                    rSelect_row=row
                    lr="R"
                else:
                    lSelect_column=column
                    lSelect_row=row
                    lr="L"
        lst.append(lr)
    answer="".join(lst)
    return answer
#numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
#hand="right"
hand="left"
result=solution(numbers,hand)
print(result)
if(result==	"LRLLRRLLLRR"):
    print("complete")

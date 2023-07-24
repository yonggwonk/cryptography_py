"""Keyword='PLAYFAIREXAMPLE'

P='helloworld'

C=E(P, Keyword)

C=='DMYRANVQCRGE'"""


abc='abcdefghijklmnopqrstuvwxyz'
ABC=abc.upper()
def Keytable_generate(K):         #키테이블 등록하는 함수
    Key_table=[[0 for i in range(5)]for j in range(5)]       #table틀 생성
    exist_letter=[]         #중복제거를 위한 리스트 생성
    x=0     #row
    y=0     #columm
    for i in K:
        if i not in exist_letter:
            exist_letter.append(i)     
        else:
            continue        
        if (y==4):
            y=0
            x+=1
        else:
            x+=1
#Keyword의 만큼 키 테이블 채워넣는 알고리즘
    for i in ABC:
        if i=='J':
            continue   #I=J로 간주
        if i not in exist_letter:
            exist_letter.append(i)
    num=0
    for i in range(5):
        for j in range(5):
            Key_table[i][j]=exist_letter[num]
            num+=1
    return Key_table

def separate_text(text):
    index=0
    while(index<len(text)):
        first=text[index]
        if index==len(text)-1:
            text=text+'x'
            index+=2
            continue
        second=text[index+1]
        if first==second:
            text=text[:index+1]+'x'+text[index+1:]
        index+=2
    return text
"""index는 짝수로 유지하며, 짝수 단위로 자른
문자열에서 같은 문자 연속 등장시 사이에 'X'추가
홀수개일 경우 끝에 X추가"""

                 
"""두 철자가 같은 세로줄: 바로 다음의 대문자 대체
두 철자가 같은 가로줄: 바로 아래의 대문자 대체
둘 다 다를 경우: 첫 철자 가로줄 수평이동, 교차하는 자리+두번째 철자 같은방식으로"""
def find_index(P,keytable):
    for i in range(5):
        try:
            index=keytable[i].index(P)
            return(i,index)
        except:
            continue
        
def E(P,K):
    keytable=Keytable_generate(K)
    P=separate_text(P)
    P=P.upper()
    result=''
    for (num1,num2) in zip(P[0::2], P[1::2]):
        row1,col1 = find_index(num1,keytable)
        row2,col2 = find_index(num2,keytable)
        if row1==row2: #행이 같은 경우
            result += keytable[row1][(col1+1)%5] + keytable[row2][(col2+1)%5]
        elif col1==col2:#열이 같은 경우
            result += keytable[(row1+1)%5][col1] + keytable[(row2+1)%5][col2]
        else: #서로 다른 행,렬에 위치할 경우
            result += keytable[row1][col2] + keytable[row2][col1]
    print(result)
    return result
                 
Keyword='PLAYFAIREXAMPLE'
P='helloworld'
C=E(P, Keyword)
C=='DMYRANVQCRGE'
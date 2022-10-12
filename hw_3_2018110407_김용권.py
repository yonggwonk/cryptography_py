"""
1. 문자열 입력
2. lengthof key 사용 후 정수 저장
3. 문자열의 길이를 K로 나눈 몫으로 2차원 배열 생성
4. 마지막 행의 열들이 비어있다면 z삽입
5. key에 따라 행 이동(index)
5.1 전치
6. 1행부터 대문자로 출력"""


import numpy as np
P='enemyattackstonight'
K=[3,1,4,5,2]

def E(P,K):  #Encryption
    columm=len(K)
    p_length=len(P)
    row=p_length//columm+1
    num=p_length%columm
    P_new=P+'z'*(columm-num)
    table=[]
    for i in range(row):
        table.append([0]*columm)     #배열 생성
    x=0
    for i in range(row):
        for j in range(columm):
            table[i][j]=P_new[x]
            x+=1
    #table 구성 완료
    new_table=[]
    for i in range(row):
        new_table.append([0]*columm)
    for i in range(row):
        for j in range(columm):
            new_table[i][j]=table[i][K[j]-1]    
    #열끼리 변환 완료
    new_table=np.array(new_table)
    T_table=new_table.T
    #전치 완료
    C=''
    for i in range(columm):
        for j in range(row):
            C+=T_table[i][j].upper()
    return C        #암호문 반환

"""
1. 2차원 배열로 저장
2. 전치
3. key에따라 이동"""

C='ETTHEAKIMAOTYCNZNTSG' 
def D(C,K):
    columm=len(K)
    c_length=len(C)
    row=c_length//columm
    table=[]
    for i in range(columm):
        table.append([0]*row)
    x=0
    for i in range(columm):
        for j in range(row):
            table[i][j]=C[x]
            x+=1
    #table 생성 완료
    new_table=np.array(table)
    T_table=new_table.T
    #전치 완료
    p_table=[]
    for i in range(row):
        p_table.append([0]*columm)
    for i in range(row):
        for j in range(columm):
            p_table[i][K[j]-1]=T_table[i][j]
    #평문 배열로 변환 완료(열 순서 바꾸기)
    P=''
    for i in range(row):
        for j in range(columm):
            P+=p_table[i][j].lower()
    return P
    #평문 반환
def E(P,K,f):
    if(len(P)%2!=0):
        print("홀수개의 비트를 암호화 할 수 없음")
    else:
        roundP=len(K)
        P_front=''
        P_back=''
        for i in range(len(P)//2):
            P_front+=P[i]
            P_back+=P[i+len(P)//2]  #둘로 쪼개기    
        
        
        for i in range(roundP-1):
            temp_back=P_back
            temp=f(P_back,K[i])
            P_back=str(int(temp[0])^int(P_front[0]))+str(int(temp[1])^int(P_front[1]))
            P_front=temp_back             #mix+swap , key의 길이 -1만큼 반복
            
        temp=f(P_back,K[roundP-1])
        P_front=str(int(temp[0])^int(P_front[0]))+str(int(temp[1])^int(P_front[1]))     #마지막 round: swapper 없음
        print("C: "+P_front+P_back)
        return P_front+P_back
def D(C,K,f):
    if(len(C)%2!=0):
        print("홀수개의 비트를 복호화 할 수 없음")
    else:
        roundC=len(K)
        C_front=''
        C_back=''
        for i in range(len(C)//2):
            C_front+=C[i]
            C_back+=C[i+len(C)//2]  #둘로 쪼개기
        
        
        for i in range(roundC-1):
            temp_back=C_back
            temp=f(C_back,K[roundC-1-i])        #key[2], key[1], ... =>역순으로 계산
            C_back=str(int(temp[0])^int(C_front[0]))+str(int(temp[1])^int(C_front[1]))
            C_front=temp_back             #mix+swap , key의 길이 -1만큼 반복
            
        temp=f(C_back,K[0])
        C_front=str(int(temp[0])^int(C_front[0]))+str(int(temp[1])^int(C_front[1]))
        print("P: "+C_front+C_back)
        return C_front+C_back
P='1011'
K=['011', '101' ]
f=lambda x, y: str(int(x[0])^int(y[1]))+str(((int(x[1])&int(y[0]))|int(y[2])))
f('10', '101')
E(P, K, f)
C='0011'
D(C, K, f)

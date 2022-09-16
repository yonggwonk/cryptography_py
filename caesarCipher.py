abc='abcdefghijklmnopqrstuvwxyz'


ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def E(P,K):

    x=''                                 

    for i in P:

        x+=ABC[(abc.index(i)+K)%26]       

    return x                              

def D(C,K):
    y=''
    for i in C:
        y+=abc[(ABC.index(i)-K)%26]
        
    return y
        

print(E('hello', 3))
print(D('KHOOR',3))
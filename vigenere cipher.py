abc='abcdefghijklmnopqrstuvwxyz'
ABC=abc.upper()

def E(p,key):
    length=len(p)
    x=''
    for i in range(length):
        k=ABC.index(key[i%len(key)])
        x+=ABC[(abc.index(p[i])+k)%26]
        
    return x

print(E('attackatdawn','LEMON'))
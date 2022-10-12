from CaesarCipher import ABC, D     #CaesarCipher import

def LFA(C):         #define LFA
    freq=[]         #variable initialize
    for i in ABC:   
        freq.append(C.count(i))   #A~Z의 개수y를 순서대로 배열로 저장 
    
    max_value=max(freq)     #빈도수의 최댓값 추출(가장 많이 나타난 알파벳)
    max_alphabet=ABC[freq.index(max_value)]     #가장 많이 나타난 알파벳을 저장
    key=ABC.index(max_alphabet)-4      
            #key값을 알파벳의 인덱스 -4로 저장(평문에서 e(4)가 가장 많이 나타나기 때문)
    print(D(C,key),"\n")        #decryption function in CaesarCipher
   
#아래는 e에 대한 빈도수 공격 실패시 시도하는 case들이다.
    for x in [19,0,14,8,13]:       #t,a,o,i,n
        next=input("다음 결과를 보시겠습니까?[y/n]\n")
        if(next=='y'):
            key=ABC.index(max_alphabet)-x       #key값을 변화시키며 결과 관찰
            print(D(C,key),"\n")
        else :
            break
        #y이외의 문자 입력시 루프 종료
            
        
LFA('LGTWGJFGLLGTWLZSLAKLZWIMWKLAGF')
# 최빈값 L이 t와 대응되는 경우, to be or not to be that is the question이라는 문장을 얻을 수 있다.

Sbox =  ( 0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76, 
          0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 
          0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15, 
          0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 
          0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 
          0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 
          0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8, 
          0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 
          0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73, 
          0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 
          0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 
          0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08, 
          0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 
          0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 
          0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 
          0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 )
 
InvSbox = (0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
           0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
           0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
           0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
           0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
           0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
           0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
           0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
           0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
           0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
           0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
           0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
           0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
           0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
           0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
           0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D)
P='00041214120412000C00131108231919'
K='2475A2B33475568831E2120013AA5487'

RC128 = [ 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]      #round const
RC192=[ 0x01, 0x01, 0x02, 0x04, 0x04, 0x08, 0x10, 0x10, 0x20, 0x40, 0x40, 0x80]
RC256=[ 0x01, 0x01, 0x01, 0x02, 0x02, 0x04, 0x04, 0x08, 0x08, 0x10, 0x10, 0x20,0x20,0x40]
if len(K) == 32:
    Nk = 4
    Nr = 10
    RC=RC128
elif len(K) == 48:
    Nk = 6
    Nr = 12
    RC=RC192
elif len(K) == 64:
    Nk = 8
    Nr = 14
    RC=RC256

# AES 10 라운드 암호화 함수
def E(P, K):
    
    key=blockToState(K)
    state=blockToState(P)
    round_key = roundKeyGenerator(key)
    new_state = AddRoundKey(state, round_key[0])
 
    for cnt_i in range(1,Nr): # 1~9라운드 반복문 처리
        out_state = Round(new_state, round_key[cnt_i])
        new_state = out_state

    rst_state1 = SubBytes(new_state)
    rst_state2 = ShiftRows(rst_state1)
    rst_state3 = AddRoundKey(rst_state2, round_key[Nr])
    text=''
    for i in range(4):
        for j in range(4):
            rst_state3[i][j]=format(rst_state3[i][j],'0x')
            text+=rst_state3[i][j]
    return text
 
def D(C,K):
    key=blockToState(K)
    state = blockToState(C)
    round_key = roundKeyGenerator(key)
    new_state = AddRoundKey(state, blockToState(round_key(Nr)))
    for i in range(Nr-1, 0, -1):
        rst_state1 = invShiftRows(new_state)
        rst_state2 = invSubBytes(rst_state1)
        rst_state3 = AddRoundKey(rst_state2, blockToState(roundKeyGenerator(i)))
        if i!=0:
            rst_state4 = invMixColumns(rst_state3)
    P = stateToblock(rst_state4)
    return P
 
# block 을 state로 변환
 
def blockToState(block):
    state = []
    for i in range(0,8,2):
        temp = []
        for j in range(0,8,2):
            col = '0x'+P[i*4+j]+P[i*4+j+1] #
            temp.append(int((col),16))
        state.append(temp)
    return state    
# SubBytes (Sbox에 맞춰 치환)
def stateToblock(state):
    block=''
    for i in range(4):
        for j in range(4):
            block+=state[i][j][2:4]
    return block
    
def SubBytes(input_state):
    state = []
    for row in range(4):
        temp = []
        for tmpnum in range(4):
            temp.append(Sbox[input_state[row][tmpnum]])
        state.append(temp)
    return state
 
def invSubBytes(input_state):
    state = []
    for row in range(4):
        temp = []
        for tmpnum in range(4):
            temp.append(InvSbox[input_state[row][tmpnum]])
        state.append(temp)
    return state
 
def ShiftRows(input_state):
    state = []
    for row in range(4):
        temp = []
        for tmpnum in range(4):
            temp.append(input_state[(row+tmpnum)%4][tmpnum])
        state.append(temp)
    return state

def invShiftRows(input_state):
    state = []
    for row in range(4):
        temp = []
        for tmpnum in range(4):
            temp.append(input_state[(row-tmpnum)%4][tmpnum])
        state.append(temp)
    return state

 
def SubByte_Col(col):
    result_col = [Sbox[col[cnt_i]] for cnt_i in range(4)]
    return result_col
 
def Xor_Col(c1, c2):
    result_col = [c1[cnt_i] ^ c2[cnt_i] for cnt_i in range(4)]
    return result_col
 
def Rotl(col):
    result_col = [col[1], col[2], col[3], col[0]]
    return result_col
 
def KeySR(col, round):
    result_col = Rotl(col)
    round_constant = [ RC[round-1], 0, 0, 0]
    result_col2 = SubByte_Col(result_col)
    result_col3 = Xor_Col(result_col2, round_constant)
    return result_col3
 
def roundKeyGenerator(key_state):
    rkey = [ key_state ]
    for round in range(1,Nr+1):
        new_state = []
        new_w0 = Xor_Col(rkey[round-1][0], KeySR(rkey[round-1][3], round))
        new_state.append(new_w0)
        new_w1 = Xor_Col(rkey[round-1][1], new_w0)
        new_state.append(new_w1)
        new_w2 = Xor_Col(rkey[round-1][2], new_w1)
        new_state.append(new_w2)
        new_w3 = Xor_Col(rkey[round-1][3], new_w2)
        new_state.append(new_w3)
        rkey.append(new_state)
    return rkey
 
 
def AddRoundKey(state , rkey):
    new_state = []
    for col in range(4):
        result_col = [Sbox[state[col][cnt_i]] for cnt_i in range (4)]
        new_state.append(result_col)
    return new_state
 
def x_time(index):
    y = (index << 1) & (0xff)
    if (index >= Nk*32):
        y ^= 0x1b
    return y
 

def multi_02(index):   # 0x02 곱하기
    return x_time(index)
 

def multi_03(index):   # 0x03 곱하기
    return multi_02(index)^index

def mixColumn_single(col):
    out_col = [0]*4
    out_col[0] = multi_02(col[0]) ^ multi_03(col[1]) ^ col[2] ^ col[3]  
    out_col[1] = col[0] ^ multi_02(col[1]) ^ multi_03(col[2]) ^ col[3]  
    out_col[2] = col[0] ^ col[1] ^ multi_02(col[2]) ^ multi_03(col[3])  
    out_col[3] = multi_03(col[0]) ^ col[1] ^ col[2] ^ multi_02(col[3])  
    return out_col
 

def mixColumns(state):
 
    out_state = []                    
    for num in range(4):                            
        out_col = mixColumn_single(state[num])     
        out_state.append(out_col)                    
    return out_state               

def invMixColumns(state):
    out_col=[]
    col = [[0x0E, 0x0B, 0x0D, 0x09],
          [0x09, 0x0E, 0x0B, 0x0D],
          [0x0D, 0x09, 0x0E, 0x0B],
          [0x0B, 0x0D, 0x09, 0x0E]]
    for i in range(4):
        for j in range(4):
            out_col[i][j] ^= col[i][j]^state[i][j]
    return out_col

def Round(state, rkey): # AES의 한 round 연산
    # SubBytes -> ShiftRows -> MiColumns -> AddRoundKey 
    new_state = state
    rst_state1 = SubBytes(new_state)
    rst_state2 = ShiftRows(rst_state1)
    rst_state3 = mixColumns(rst_state2)
    rst_state4 = AddRoundKey(rst_state3, rkey)
 
    return rst_state4
 


 

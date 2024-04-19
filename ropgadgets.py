from capstone import *
from tqdm import tqdm
import pickle

default = "./res.rop"
def brief(x,keywords):
    m = 0x7ffffffff
    M = -1
    Ml = 0
    for i in keywords:
        if m > x.index(i):
            m = x.index(i)
        if M < x.index(i):
            M = x.index(i)
            Ml = len(i)
    if m == -1 or M == -1:
        return None
    s,S = 0,0
    if M+Ml+1 > len(x):
        S = 1
    if m-21 < 0:
        s = 1
    if s and not S:
        return x[:M+Ml+1]
    elif not s and S:
        i = m
        while True:
            if x[i] == '\n':
                i+=1
                break
            i-=1
        return x[i:]
    elif not s and not S:
        i = m
        while True:
            if x[i] == '\n':
                i+=1
                break
            i-=1
        return x[i:M+Ml+1]
    else:
        return x
    
def parse_int(v):
    if v.startswith("0x"):
        v = int(v,16)
    else:
        v = int(v,10)
    return v
def search(s,sv):
    if sv:
        print("save? (y/n) : ",end='')
        v = input() == 'y'
        if v: 
            with open(default,"wb") as f:
                pickle.dump(s, f)
            print("saved")
    print()
    print("Examples)\n\t1) array search :\n\t\tSearch > ['xchg','esp','ret']\n\t2) string search :\n\t\tSearch > xchg esp\n\t3) quit :\n\t\tSearch > q\n\t4) Save results :\n\t\tSearch > save")
    print()
    while True:
        print("Search > ",end='')
        v = input()
        if v == 'q':
            break
        elif v.startswith('['):
            print("limit : ",end='')
            limit = parse_int(input())
            arr = eval(v)
            res = []
            for i in s:
                f = 0
                cur = -1
                idx = []
                for j in arr:
                    if j not in i:
                        f = 1
                        break
                    else:
                        if cur < i.index(j):
                            if i.index(j) not in idx:
                                idx.append(i.index(j))
                                cur = i.index(j)
                        else:
                            f = 1
                if f==0:
                    m = sum(idx) / len(idx)
                    M = 0
                    t = 0
                    for k in idx:
                        t = (m - k)**2
                        if M < t:
                            M = t
                    res.append([t,i])
            print("show brief (y/n) : ",end= '')
            v = input() == 'y'
            res.sort()
            if len(res) < limit:
                limit = len(res)
            for i in range(limit):
                if v:
                    print()
                    x= brief((res[i][1]),arr)
                    if x == None:
                        continue
                    print(x)
                else:
                    print()
                    print((res[i][1]))
        else:
            print("limit : ",end='')
            limit = parse_int(input())
            for i in s:
                if v in i:
                    print(i)

if __name__ == '__main__':
    with open('./asdf.bin', 'rb') as f:
        mem = f.read()
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    #gadgets = [b'\xc3',b"\xc2",b'\xcb',b"\xca",b'\xf2\xc3',b"\xf2\xc2",b'\xff',b'\xeb',b'\xe9',b'\xf2\xff',b'\xcd\x80',b"\x0f\x34",b"\x0f\x05",b'\x65\xff\x15\x10\x00\x00\x00']
    gadgets = [b'\xc3',b"\xc2",b'\xcb',b"\xca",b'\xff',b'\xeb',b'\xe9',b'\xf2',b'\xcd',b'\x0f',b'\x65',b'\x48'] # iretq
    candi = []
    print("finding gadgets")
    for i in tqdm(range(len(mem))):
        for k in gadgets:
            if mem[i] == k[0]:
                candi.append(i)
    s = []
    base = 0x0
    # print("width : ",end='')
    # v = parse_int(input())
    v = 0x20 # width 0x20 by default
    print("disassembling")
    for j in tqdm(range(len(candi))):
        tmp = ''
        if j-v < 0:
            for i in md.disasm(mem[:candi[j]+v], base):
                tmp += ("%s:\t%s %s\n" %('0x'+hex(i.address).replace('0x','').zfill(16) + ' (+'+ hex(i.address-base)+')', i.mnemonic, i.op_str))
        else:
            for i in md.disasm(mem[candi[j]-v:candi[j]+v], base+candi[j]-v):
                tmp += ("%s:\t%s %s\n" %('0x'+hex(i.address).replace('0x','').zfill(16) + ' (+'+ hex(i.address-base)+')', i.mnemonic, i.op_str))
        s.append(tmp)
    search(s,True)

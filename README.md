# ropgadgets_by_addr
 
```
pwndbg> source ../rop_by_addr.py
load? (y/n) : n
segment address : 0xffffffffb62fc0f0
reading memory 0xffffffffb6200000 ~ 0xffffffffb7403000 (0x1203000 bytes)
finding gadgets
100%|██████████████████████████████████████████████████████████████████| 18886656/18886656 [00:24<00:00, 785525.45it/s]
disassembling
100%|█████████████████████████████████████████████████████████████████████| 1752054/1752054 [01:49<00:00, 15950.41it/s]
save? (y/n) : y
saved

Examples)
        1) array search :
                Search > ['xchg','esp','ret']
        2) string search :
                Search > xchg esp
        3) quit :
                Search > q
        4) Save results :
                Search > save

Search > ['xchg','esp','ret']
limit : 10
show brief (y/n) : y

0xffffffffb67616cd:     xchg eax, esp
0xffffffffb67616ce:     ret

0xffffffffb67c9d7b:     xchg eax, esp
0xffffffffb67c9d7c:     ret

0xffffffffb67fdbaf:     xchg eax, esp
0xffffffffb67fdbb0:     ret

0xffffffffb67fdbaf:     xchg eax, esp
0xffffffffb67fdbb0:     ret

0xffffffffb6ad2a09:     xchg eax, esp
0xffffffffb6ad2a0a:     ret

0xffffffffb6ad2a09:     xchg eax, esp
0xffffffffb6ad2a0a:     ret

0xffffffffb6c8d6f0:     xchg eax, esp
0xffffffffb6c8d6f1:     ret

0xffffffffb6cee077:     xchg eax, esp
0xffffffffb6cee078:     ret

0xffffffffb6cee1c1:     xchg eax, esp
0xffffffffb6cee1c2:     ret

0xffffffffb6218e4e:     xchg eax, esp
0xffffffffb6218e4f:     ret
Search > q
pwndbg>
```

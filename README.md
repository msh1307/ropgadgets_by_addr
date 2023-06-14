# ropgadgets_by_addr
 
```
pwndbg> source ./rop_by_addr.py
load? (y/n) : y
loaded successfully

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
limit : 4
show brief (y/n) : y

0xffffffff8cbfdbcf:     xchg eax, esp
0xffffffff8cbfdbd0:     ret

0xffffffff8c66a423:     xchg eax, esp
0xffffffff8c66a424:     ret

0xffffffff8ca7c801:     xchg eax, esp
0xffffffff8ca7c802:     ret

0xffffffff8cb616ab:     xchg eax, esp
0xffffffff8cb616ac:     ret
Search >
```

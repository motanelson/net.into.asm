printf "\x1bc\x1b[47;31m\ngive me the x86 .exe from net\n"
read a
objdump --disassembler-options=intel -D $a

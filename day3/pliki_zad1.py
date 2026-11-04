# działąnia z plikami
# filehandler

# context manager
#  with - kontekst menadżer w pythonie

# open()
with open("test.log", "w", encoding="utf-8") as f:
    f.write('Powitanie\n')
    f.write('Powitanie jeszcze jedno\n')

# f.write("")  # ValueError: I/O operation on closed file.

# x
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x",  encoding="utf-8") as f:
#     f.write('Powitanie\n')
#     f.write('Powitanie jeszcze jedno\n')

# a
with open("test.log", "a", encoding="utf-8") as f:
    f.write('Powitanie\n')
    f.write('Powitanie jeszcze jedno\n')
    f.write('Dośdane\n')

with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
# chardet
# Universal character encoding detector.

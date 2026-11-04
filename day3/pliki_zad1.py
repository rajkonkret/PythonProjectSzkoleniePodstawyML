# działąnia z plikami
# filehandler

# context manager
#  with - kontekst menadżer w pythonie

# open()
with open("test.log", "w") as f:
    f.write('Powitanie\n')
    f.write('Powitanie jeszcze jedno\n')

# f.write("")  # ValueError: I/O operation on closed file.

# x
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x") as f:
#     f.write('Powitanie\n')
#     f.write('Powitanie jeszcze jedno\n')

# a
with open("test.log", "a") as f:
    f.write('Powitanie\n')
    f.write('Powitanie jeszcze jedno\n')
    f.write('Dodane\n')
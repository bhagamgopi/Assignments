string = '''A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together'''


wrd_lst = string.split()
n = len(wrd_lst)

count = 0
res = ""

while(count < n):
    if count % 2 == 0:
        res = res + " " + wrd_lst[count].upper()
    else:
        res = res + " " + wrd_lst[count]
    count  += 1

print(res)

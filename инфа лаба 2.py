from math import log2
string = input("Введите классический код Хэмминга:\n")
code = [i == '1' for i in string]

s = ""
for I in range(int(log2(len(code))+1)):
    st = False
    for i in range(0, len(code)):
        if (i+1) % 2**(I+1) >= 2**I:
            st = st != code[i]
    st = str(int(st))
    s = st + s

s = int(s, 2) - 1
if s!= -1:
    print("Ошибка в бите №" + str(s + 1))
    string = string[:s] + str(abs(int(string[s])-1)) + string[s + 1:]
    print("Исправленный код: ")
    for i in range(len(string)):
        if log2(i+1)%1 != 0:
            print(string[i], end='')
else:
    print('Код исправен')


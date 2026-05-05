s = 0
con = 0
for c in range(1, 501, 2):
    if c %3==0:
        s +=c
        con = con + 1
print('A soma de todos os {} valores é: {}'.format(con,s))

s = 0
c = 0
for x in range(0,501):
    if x % 2 != 0 and x %3 == 0:
        s+=x
        c = c+1
print('A soma de todos os {} valores dá: {}'.format(c,s))
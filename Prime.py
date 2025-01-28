num = 11
flag = False

for i in range (2 , num):
    if (num % i) == 0:
        flag = True
        break

if flag is True:
    print('It Is A Not Prime Number')

else:
    print('It is a Prime Number')


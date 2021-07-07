import random
num = 0
sum = 0
min = 0
max = 0
var = 0
DieOne = 0
DieTwo = 0

while DieOne != 6 or DieTwo != 6:
    num = num + 1
    DieOne = random.randint(1, 6)
    DieTwo = random.randint(1, 6)
    print(DieOne)
    print(DieTwo)
    print()
    if (DieOne == 6) and (DieTwo == 6):
        num = str(num)
        print('You got double 6s in ' + num + ' tries!')
        print()
    for var in range(1, 12, 1):
        sum = sum + var
        print(sum)
# output: You got double 6s in 30 tries!
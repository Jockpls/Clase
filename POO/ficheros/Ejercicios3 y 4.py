name = open('nombres.txt', 'r')
line = name.readline()
numlin = 0
while line != '':
    if numlin == 0:
        print(f'Aquí tiene, {line.rstrip()}')
        numlin += 1
    else:
        print(f'El nombre {numlin} es {line.rstrip()}, eres un tiaco.')
        numlin += 1
        line = name.readline()
name.close()
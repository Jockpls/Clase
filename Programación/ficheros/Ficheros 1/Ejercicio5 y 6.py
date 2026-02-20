lenguajes = ['Python','Java','JS','Cobol','CSS','C##']

lengua = open('lenguajes.txt','wt+')
for i in range(0,len(lenguajes)):
    if i == len(lenguajes):
        lengua.write(i)
    else:
        lengua.write(lenguajes[i] + f'\n')
lengua.seek(0)
leer = lengua.read()
print(leer)
lengua.close()

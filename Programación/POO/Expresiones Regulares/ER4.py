import re
regex_cp = ""
cp =  input("Ingrese su código postal: ")
if re.fullmatch('[0-9]{5}', cp):
    print('Correcto')
else:
    print('Incorrecto')
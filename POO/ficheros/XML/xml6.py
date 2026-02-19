import xml.etree.ElementTree as ET

archivo = 'clientes.xml'
tree = ET.parse(archivo)
root = tree.getroot()



def opciones():
    print(f"--- Menú ---\n1. Añadir cliente\n2. Listar clientes\n3. Buscar cliente\n4. Eliminar cliente\n5. Salir')

def menu():
    while opciones != "5":
    opciones()
    option = input('¿Qué desea hacer?')
        match option:
            case 1:#Añadir

            case 2:#Listar

            case 3:#Buscar

            case 4: #Eliminar

import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml4 import showdept

class UserNotFoundError(Exception):
    pass

def main():
    archivo = 'clientes.xml'
    tree = ET.parse(archivo)
    root = tree.getroot()

    def dropclient():
        cliente = input('Introduce el DNI del cliente que quiere eliminar: ')
        for client in root.findall('cliente'):
            if client.get('dni') == cliente:
                cliente = client
        try:
            if cliente is True:
                root.remove(cliente)
                tree.write('clientes.xml')
                print('El cliente ha sido eliminado satisfactoriamente.')
            else:
                raise UserNotFoundError('Usuario no encontrado')
        except UserNotFoundError as e:
            print(e)


    def addclient():
        dni = input('Introduce el DNI: ')
        nombre = input('Introduce el nombre: ')
        mail = input('Introduce el mail: ')
        cliente = ET.Element('cliente')
        ET.SubElement(cliente, 'dni').text = dni
        ET.SubElement(cliente, 'nombre').text = nombre
        ET.SubElement(cliente, 'mail').text = mail
        root.append(cliente)

        xml_bytes = ET.tostring(root, encoding='utf-8')
        xml_pretty = minidom.parseString(xml_bytes).toprettyxml()
        with open('clientes.xml', 'w') as xml_file:
            xml_file.write(xml_pretty)
        print('Cliente añadido con exito')

    def opciones():
        print(f"--- Menú ---\n1. Añadir cliente\n2. Listar clientes\n3. Buscar cliente\n4. Eliminar cliente\n5. Salir')

    def menu():
        while option != "5":
            opciones()
            option = input('¿Qué desea hacer?')
            match option:
                case 1:#Añadir
                    addclient()
                case 2:#Listar

                case 3:#Buscar
                    search = input('Introduce el DNI del cliente: ')
                    showdept(search)
                case 4: #Eliminar
                    dropclient()
if __name__=="__main__":
    main()
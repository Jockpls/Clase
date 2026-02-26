import xml.etree.ElementTree as ET
from xml.dom import minidom

def showdept(root, departmento):
    print(f"\nResultados para {departmento}")
    for emp in root.findall('empleado'):
        if emp.get('departamento') == departmento:
            nombre = emp.find('nombre').text
            salario = emp.find('salario').text
            print(f"\nNombre: {nombre} (ID:{emp.get('id')}): {salario}€ )")

def main():
    archivo = "empleados.xml"
    tree = ET.parse(archivo)
    root = tree.getroot()

    employee = ET.Element('empleado')
    employee.set('id','3')
    employee.set('departamento', "IT")
    ET.SubElement(employee, 'nombre').text = 'Elver Galarga'
    ET.SubElement(employee, 'salario').text = '1896'
    root.append(employee)

    xml_bytes = ET.tostring(root, encoding='utf-8')
    xml_pretty = minidom.parseString(xml_bytes).toprettyxml()
    with open('productos.xml', 'w') as xml_file:
        xml_file.write(xml_pretty)

    departmento = input('¿De qué departamento desea ver los empleados? ')
    showdept(root, departmento)

if __name__ == "__main__":
    main()
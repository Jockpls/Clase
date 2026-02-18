import xml.etree.ElementTree as ET
from xml.dom import minidom

Empresa = "empleados.xml"
tree = ET.parse(Empresa)
root = tree.getroot()

def showdept(departmento):
    for root.attrib['departamento'] in empleado:
        

employee = ET.Element('empleado')
ET.Element.attrib['ID'] = '3'
ET.Element.attrib['Departamento'] = "IT"
ET.SubElement(employee, 'nombre').text = 'Elver Galarga'
ET.SubElement(employee, 'salario').text = '1896'

Tree = ET.ElementTree(root)

xml_bytes = ET.tostring(root, encoding='utf-8')
xml_pretty = minidom.parseString(xml_bytes).toprettyxml()
with open('productos.xml', 'w') as xml_file:
    xml_file.write(xml_pretty)

departmento = input('¿De qué departamento desea ver los empleados?')
showdept(departmento)


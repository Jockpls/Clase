import xml.etree.ElementTree as ET
from xml.dom import minidom

libreria = "libros.xml"

tree = ET.parse(libreria)
root = tree.getroot()

print(f'---Añadimos libros---')
for libreria in range(3):
    titulo = input('Ingrese tu titulo: ')
    autor = input('Ingrese tu autor: ')
    precio = input('Ingrese precio: ')

    book = ET.Element('libro')
    ET.SubElement(book, 'titulo').text = titulo
    ET.SubElement(book, 'autor').text = autor
    ET.SubElement(book, 'precio').text = precio
    root.append(book)
    print(f'Libro añadido.\n')

for librillo in root:
    print(f'{librillo.tag}')
    for child in librillo:
        print(f'{child.tag}: {child.text}')

tree = ET.ElementTree(root)

xml_bytes = ET.tostring(root, encoding='utf-8')
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent='    ')

with open('libros.xml', 'w') as xml_file:
    xml_file.write(xml_pretty)








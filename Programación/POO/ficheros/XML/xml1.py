import xml.etree.ElementTree as ET

XML = "ficheropartida.xml"

tree = ET.parse(XML)
root = tree.getroot()

print(f'Etiqueta raíz: {root.tag}\n')
alumns = 0
for book in root:
    print(f'Nodo: {book.tag}:')
    if book.tag == 'alumno':
        alumns += 1
    for child in book:
        print(f'- {child.tag}: {child.text}')
print(f'Hay {alumns} alumnos')
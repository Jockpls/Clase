import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('Productos')

producr1 = ET.SubElement(root,'Producto')
ET.SubElement(producr1, 'Nombre').text = 'Teclado'
ET.SubElement(producr1, 'Precio').text = '20'

producr2 = ET.SubElement(root,'Producto')
ET.SubElement(producr2, 'Nombre').text = 'Raton'
ET.SubElement(producr2, 'Precio').text = '10'

for producto in root:
    print(f'{root.tag}')
    for child in producto:
        print(f'{child.tag}: {child.text}')

tree = ET.ElementTree(root)

xml_bytes = ET.tostring(root, encoding='utf-8')
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent = '  ')

with open('productos.xml', 'w') as product:
    product.write(xml_pretty)

prod = "productos.xml"
tree = ET.parse(prod)
root = tree.getroot()

price = float(root.find('Producto').find('Precio').text)
for producto in root:
    print(f'{root.tag}')
    for child in producto:
        if child.tag == 'Precio':
            precio_actual = float(child.text)
            precio_nuevo = precio_actual * 1.1
            print(f'{producto.find('Nombre').text}: {precio_nuevo:.2f}')
            child.text = str(round(precio_nuevo, 2))

tree.write('productos.xml', encoding='utf-8')
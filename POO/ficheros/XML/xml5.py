import xml.etree.ElementTree as ET


archivo = 'tienda.xml'
tree = ET.parse(archivo)
root = tree.getroot()

for obj in root.findall('producto'):
    cantidad = obj.get('stock')
    if cantidad == '0':
        root.remove(obj)
    print(obj)

tree.write(archivo)

pedidos = [
    {"cliente": "Ana", "producto": "Portátil", "precio": 1000, "cantidad": 1},
    {"cliente": "Luis", "producto": "Ratón", "precio": 25, "cantidad": 2},
    {"cliente": "Ana", "producto": "Teclado", "precio": 50, "cantidad": 1},
]

for p in pedidos:
    cliente = p["cliente"]
    producto = p["producto"]
    precio = p["precio"]
    cantidad = p["cantidad"]

    subtotal = precio * cantidad

    descuento = 0
    if subtotal > 500:
        descuento = subtotal * 0.1

    subtotal = subtotal - descuento

    iva = subtotal * 0.21
    total = subtotal + iva

    print("Cliente:", cliente)
    print("Producto:", producto)
    print("Cantidad:", cantidad)
    print("Subtotal:", precio * cantidad)
    print("Descuento:", descuento)
    print("IVA:", iva)
    print("Total:", total)
    print("-------------------------")
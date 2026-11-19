def total_facturado(ventas):
    return sum(venta["cantidad"] * venta["precio_unitario"] for venta in ventas)


def ventas_por_categoria(ventas):
    unidades = {}
    for venta in ventas:
        categoria = venta["categoria"]
        unidades[categoria] = unidades.get(categoria, 0) + venta["cantidad"]
    return unidades


def producto_mas_vendido(ventas):
    unidades = {}
    for venta in ventas:
        producto = venta["producto"]
        unidades[producto] = unidades.get(producto, 0) + venta["cantidad"]
    return max(unidades.items(), key=lambda producto: producto[1], default=None)

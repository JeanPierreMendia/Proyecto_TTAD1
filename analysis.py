def total_facturado(ventas):
    """Calcula el importe total de las ventas."""
    return sum(venta["cantidad"] * venta["precio_unitario"] for venta in ventas)


def ventas_por_categoria(ventas):
    """Devuelve las unidades vendidas por categoría."""
    unidades = {}
    for venta in ventas:
        categoria = venta["categoria"]
        unidades[categoria] = unidades.get(categoria, 0) + venta["cantidad"]
    return unidades


def producto_mas_vendido(ventas):
    """Devuelve el producto con más unidades y su cantidad, o None sin ventas."""
    unidades = {}
    for venta in ventas:
        producto = venta["producto"]
        unidades[producto] = unidades.get(producto, 0) + venta["cantidad"]
    return max(unidades.items(), key=lambda producto: producto[1], default=None)

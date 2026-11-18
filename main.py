import json
from pathlib import Path

from analysis import producto_mas_vendido, total_facturado, ventas_por_categoria


def main():
    ruta_datos = Path(__file__).with_name("data.json")
    with ruta_datos.open(encoding="utf-8") as archivo:
        ventas = json.load(archivo)["ventas"]

    print(f"Total facturado: {total_facturado(ventas):.2f}")
    print("Unidades vendidas por categoría:")
    for categoria, cantidad in ventas_por_categoria(ventas).items():
        print(f"  {categoria}: {cantidad}")

    resultado = producto_mas_vendido(ventas)
    if resultado is None:
        print("No hay ventas registradas.")
    else:
        producto, cantidad = resultado
        print(f"Producto más vendido: {producto} ({cantidad} unidades)")


if __name__ == "__main__":
    main()

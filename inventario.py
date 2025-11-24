

import datetime


inventario = [
    {"nombre": "Laptop", "marca": "Dell", "categoria": "Computo", "precio": 2500, "cantidad": 10, "garantia": 12},
    {"nombre": "Mouse", "marca": "Logitech", "categoria": "Accesorios", "precio": 25, "cantidad": 50, "garantia": 6},
    {"nombre": "Teclado", "marca": "HyperX", "categoria": "Accesorios", "precio": 45, "cantidad": 30, "garantia": 6},
    {"nombre": "Celular", "marca": "Samsung", "categoria": "Telefonia", "precio": 900, "cantidad": 15, "garantia": 12},
    {"nombre": "Audifonos", "marca": "Sony", "categoria": "Audio", "precio": 70, "cantidad": 20, "garantia": 8},
]

ventas = []



def registrar_producto():
    try:
        nombre = input("Nombre: ")
        marca = input("Marca: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        garantia = int(input("Garantía (meses): "))

        if precio < 0 or cantidad < 0 or garantia < 0:
            print("Valores no pueden ser negativos.")
            return

        inventario.append({
            "nombre": nombre,
            "marca": marca,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad,
            "garantia": garantia
        })
        print("Producto registrado correctamente.\n")
    except ValueError:
        print("Error: Debes ingresar números válidos.\n")


def consultar_inventario():
    print("\n--- INVENTARIO ---")
    for p in inventario:
        print(p)
    print()


def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            try:
                p["precio"] = float(input("Nuevo precio: "))
                p["cantidad"] = int(input("Nueva cantidad: "))
                p["garantia"] = int(input("Nueva garantía: "))
                print("Producto actualizado.\n")
                return
            except:
                print("Error en la entrada.\n")
                return
    print("Producto no encontrado.\n")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Producto eliminado.\n")
            return
    print("Producto no encontrado.\n")


def registrar_venta():
    cliente = input("Cliente: ")
    tipo = input("Tipo de cliente: ")
    producto = input("Producto vendido: ")

    for p in inventario:
        if p["nombre"].lower() == producto.lower():
            try:
                cantidad = int(input("Cantidad: "))
                descuento = float(input("Descuento (%): "))

                if cantidad <= 0 or descuento < 0:
                    print("Valores inválidos.")
                    return

                if p["cantidad"] < cantidad:
                    print("No hay suficiente stock.\n")
                    return

                
                p["cantidad"] -= cantidad

                venta = {
                    "cliente": cliente,
                    "tipo": tipo,
                    "producto": p["nombre"],
                    "cantidad": cantidad,
                    "fecha": str(datetime.date.today()),
                    "descuento": descuento,
                    "total": p["precio"] * cantidad * (1 - descuento / 100)
                }
                ventas.append(venta)
                print("Venta registrada correctamente.\n")
                return
            except:
                print("Error en la entrada.\n")
                return

    print("Producto no encontrado.\n")


def consultar_ventas():
    print("\n--- HISTORIAL DE VENTAS ---")
    for v in ventas:
        print(v)
    print()


def top_3_productos():
    conteo = {}

    for v in ventas:
        conteo[v["producto"]] = conteo.get(v["producto"], 0) + v["cantidad"]

    ranking = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n--- TOP 3 MÁS VENDIDOS ---")
    for prod, cant in ranking:
        print(prod, "-", cant)
    print()


def ventas_por_marca():
    agrupado = {}

    for v in ventas:
        marca = ""
        for p in inventario:
            if p["nombre"] == v["producto"]:
                marca = p["marca"]
                break

        agrupado[marca] = agrupado.get(marca, 0) + v["total"]

    print("\n--- VENTAS POR MARCA ---")
    for m, total in agrupado.items():
        print(m, ":", total)
    print()


def ingresos():
    bruto = sum(v["total"] for v in ventas)
    neto = sum(v["total"] * 0.9 for v in ventas)

    print("\nIngresos brutos:", bruto)
    print("Ingresos netos (10% costos):", neto, "\n")


def rendimiento_inventario():
    print("\n--- RENDIMIENTO DEL INVENTARIO ---")
    for p in inventario:
        vendido = sum(v["cantidad"] for v in ventas if v["producto"] == p["nombre"])
        print(f"{p['nombre']}: vendido {vendido}, stock actual {p['cantidad']}")
    print()



def menu():
    while True:
        print("""
--- MENÚ PRINCIPAL ---
1. Registrar producto
2. Consultar inventario
3. Actualizar producto
4. Eliminar producto
5. Registrar venta
6. Consultar ventas
7. Reporte: Top 3 productos
8. Reporte: Ventas por marca
9. Reporte: Ingresos
10. Reporte: Rendimiento del inventario
0. Salir
""")
        try:
            op = int(input("Opción: "))
        except:
            print("Ingresa un número válido.\n")
            continue

        if op == 1: registrar_producto()
        elif op == 2: consultar_inventario()
        elif op == 3: actualizar_producto()
        elif op == 4: eliminar_producto()
        elif op == 5: registrar_venta()
        elif op == 6: consultar_ventas()
        elif op == 7: top_3_productos()
        elif op == 8: ventas_por_marca()
        elif op == 9: ingresos()
        elif op == 10: rendimiento_inventario()
        elif op == 0:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")


menu()


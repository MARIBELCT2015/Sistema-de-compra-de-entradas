#Maribel Cifuentes Torres
#Título: Sistema de compra de entradas para El Campín
#Objetivo: Calcular el total a pagar por la compra de entradas para un partido de fútbol en el estadio El Campín.
#Entradas: Código del sector y cantidad de boletas.
#Salidas: Total
#Restricciones: El código del sector debe ser A, B, C, D o E. La cantidad de boletas debe ser un número entero positivo.
# Diccionario con los sectores y precios. Se usa un diccionario para almacenar los precios.


# 🔹 CONSTANTES
PRECIOS = {
    "A": 15000,
    "B": 13000,
    "C": 10000,
    "D": 11000,
    "E": 20000
}

MENSAJE_BIENVENIDA = """
Bienvenido al sistema de compra de entradas para El Campín
Sectores disponibles:
A - Norte alta: $15.000
B - Norte baja: $13.000
C - Oriental alta: $10.000
D - Occidental alta: $11.000
E - Exclusivo: $20.000
"""

# 🔹 FUNCIONES
def mostrar_menu():
    """Muestra las opciones de sectores disponibles"""
    print(MENSAJE_BIENVENIDA)

def obtener_sector():
    """Solicita y valida el sector ingresado por el usuario."""
    while True:
        sector = input("Ingrese el código del sector (A, B, C, D, E): ").strip().upper()
        if sector in PRECIOS:
            return sector
        print("❌ Error: Sector no válido, intente de nuevo.")

def obtener_cantidad():
    """Solicita y valida la cantidad de boletas ingresada."""
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de boletas a comprar: "))
            if cantidad > 0:
                return cantidad
            print("❌ Error: La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("❌ Error: Debe ingresar un número entero.")

def calcular_total(sector, cantidad):
    """Calcula el total a pagar basado en el sector y la cantidad de boletas."""
    return PRECIOS[sector] * cantidad

def mostrar_resumen(sector, cantidad, total):
    """Muestra el resumen de la compra."""
    print("\n--- RESUMEN DE COMPRA ---")
    print(f"Sector seleccionado: {sector}")
    print(f"Precio unitario de la boleta: ${PRECIOS[sector]}")
    print(f"Cantidad de entradas compradas: {cantidad}")
    print(f"Total a pagar: ${total}")

# 🔹 FUNCIÓN PRINCIPAL
def main():
    """Función principal que ejecuta el sistema de compra de entradas."""
    while True:
        mostrar_menu()
        sector = obtener_sector()
        cantidad = obtener_cantidad()
        total_pagar = calcular_total(sector, cantidad)

        mostrar_resumen(sector, cantidad, total_pagar)

        # Preguntar si el usuario desea realizar otra compra
        repetir = input("\n¿Desea realizar otra compra? (Sí/No): ").strip().lower()
        if repetir not in ["si", "s"]:
            print("\n🎉 Gracias por su compra. ¡Disfrute el partido!")
            break

# 🔹 EJECUTAR PROGRAMA
if __name__ == "__main__":
    main()

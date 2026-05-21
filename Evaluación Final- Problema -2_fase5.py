# =================================================================
# Nombre del estudiante: Jojan Alejandro Valbuena
# Curso: Fundamentos de Programación - UNAD
# Fase 5: Evaluación Final POA - Problema 2
# Enfoque: Programación Estructurada (Funciones y Matrices)
# =================================================================

# Matriz de datos: [Nombre del Producto, Categoría, Precio Base]
# Se definen 6 productos con diversas categorías para evaluar la lógica
MENU_RESTAURANTE = [
    ["Bandeja Paisa", "Platos Fuertes", 25000],
    ["Ajiaco Santaferereño", "Platos Fuertes", 22000],
    ["Arroz con Pollo", "Platos Fuertes", 18000],
    ["Limonada de Coco", "Bebidas", 8000],
    ["Flan de Caramelo", "Postres", 12000],
    ["Porción de Empanadas", "Entradas", 10000]
]

# Constantes para la Lógica de Negocio
CATEGORIA_OBJETIVO = "Platos Fuertes"
UMBRAL_PRECIO = 20000
PORCENTAJE_DESCUENTO = 0.15

# Índices para acceder a las columnas de la matriz de forma clara
INDICE_NOMBRE = 0
INDICE_CATEGORIA = 1
INDICE_PRECIO_BASE = 2


def calcular_precio_final(producto):
    """
    Módulo que calcula el precio final de un producto aplicando la promoción.
    REQUISITO: Aplica 15% de descuento si cumple con la categoría objetivo
    Y además su precio base es estrictamente mayor al umbral definido.
    """
    categoria = producto[INDICE_CATEGORIA]
    precio_base = producto[INDICE_PRECIO_BASE]
    
    # Validación con operador lógico 'and' (Ambas condiciones obligatorias)
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        descuento = precio_base * PORCENTAJE_DESCUENTO
        precio_final = precio_base - descuento
    else:
        # Mantiene el precio base si no cumple los requisitos de la promoción
        precio_final = precio_base
        
    return precio_final


def generar_reporte_menu():
    """
    Módulo principal que recorre la matriz y genera la salida en consola.
    """
    print("=================================================================")
    print("                GESTIÓN DE PRECIOS - RESTAURANTE                 ")
    print(f" Promoción: 15% OFF en '{CATEGORIA_OBJETIVO}' mayores a ${UMBRAL_PRECIO:,}")
    print("=================================================================\n")
    
    # Encabezados de la tabla formateados para alineación visual
    print(f"{'PRODUCTO':<23} | {'CATEGORÍA':<15} | {'P. BASE':<10} | {'P. FINAL':<10}")
    print("-" * 68)
    
    # Ciclo iterativo para recorrer cada fila (producto) de la matriz
    for producto in MENU_RESTAURANTE:
        nombre = producto[INDICE_NOMBRE]
        categoria = producto[INDICE_CATEGORIA]
        precio_base = producto[INDICE_PRECIO_BASE]
        
        # Llamado al módulo de cálculo
        precio_final = calcular_precio_final(producto)
        
        # Impresión formateada con separador de miles para los precios
        print(f"{nombre:<23} | {categoria:<15} | ${precio_base:<9,} | ${int(precio_final):<9,}")
        
    print("\n=================================================================")


# Punto de entrada oficial para la ejecución del script
if __name__ == "__main__":
    generar_reporte_menu()
#Crear un programa en Python que permita al usuario ingresar sus ingresos mensuales estimados y sus gastos
#mensuales estimados por categorías, para luego calcular el balance (ahorro o déficit) y mostrar un resumen.

# Validación para la entrada de ingresos
while True:
    try:
        ingresos = float(input("Ingrese sus ingresos mensuales estimados: "))
        if ingresos < 0:
            print("Los ingresos no pueden ser negativos. Inténtelo de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

expense_categories = {}

def agregar_gasto(expense_categories):
    """
    Solicita al usuario ingresar una categoría de gasto y su monto,
    valida la entrada y agrega el gasto a la lista de categorías.
    """
    while True:
        categoria = input("Ingrese la categoría del gasto: ").strip()
        if not categoria:
            print("La categoría no puede estar vacía. Inténtelo de nuevo.")
            continue
        try:
            monto = float(input(f"Ingrese el monto para {categoria}: "))
            if monto < 0:
                print("El monto no puede ser negativo. Inténtelo de nuevo.")
                continue
            expense_categories[categoria] = monto
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def calcular_balance(ingresos, expense_categories):
    """
    Calcula el balance financiero mensual basado en los ingresos y los gastos.

    Args:
        ingresos (float): Los ingresos mensuales estimados.
        expense_categories (dict): Un diccionario con categorías de gastos como claves y montos como valores.

    Returns:
        tuple: Una tupla que contiene el total de gastos (float) y el balance (float).
    """
    total_gastos = sum(expense_categories.values())
    balance = ingresos - total_gastos
    return total_gastos, balance

def mostrar_resumen(ingresos, total_gastos, balance, expense_categories):
    """
    Muestra un resumen del presupuesto, incluyendo los ingresos,
    los gastos por categoría y el balance final.

    Args:
        ingresos (float): Los ingresos mensuales estimados.
        total_gastos (float): La suma total de los gastos.
        balance (float): La diferencia entre ingresos y gastos.
        expense_categories (dict): Diccionario de gastos.
    """
    print("\nResumen del Presupuesto:")
    print(f"Ingresos Mensuales: ${ingresos:.2f}")
    print("Gastos por Categoría:")
    if expense_categories:
        for categoria, monto in expense_categories.items():
            print(f"  {categoria}: ${monto:.2f}")
    else:
        print("  No se han registrado gastos en ninguna categoría.")

    print(f"Total de Gastos: ${total_gastos:.2f}")
    print(f"Balance Final: ${balance:.2f}")
    if balance > 0:
        print(f"¡Felicidades! Tienes un superávit de ${balance:.2f}. ¡Buen trabajo ahorrando!")
    elif balance < 0:
        print(f"¡Atención! Tienes un déficit de ${abs(balance):.2f}. Es momento de revisar tus gastos.")
    else:
        print("Tu balance es cero. Has equilibrado tus ingresos y gastos.")

# Fin de la función

if __name__ == "__main__":
    # Programa principal
    keep_adding_expenses = True

    while keep_adding_expenses:
        agregar_gasto(expense_categories)
        continuar = input("¿Desea agregar otro gasto? (s/n): ").strip().lower()
        if continuar != 's':
            keep_adding_expenses = False

    total_gastos, balance = calcular_balance(ingresos, expense_categories)
    mostrar_resumen(ingresos, total_gastos, balance, expense_categories)
    # Fin del programa

producto1_nombre = input("Ingrese el nombre del primer producto: ")
producto1_precio = float(input("Ingrese el precio del primer producto: "))

producto2_nombre = input("Ingrese el nombre del segundo producto: ")
producto2_precio = float(input("Ingrese el precio del segundo producto: "))

producto3_nombre = input("Ingrese el nombre del tercer producto: ")
producto3_precio = float(input("Ingrese el precio del tercer producto: "))

# Cálculo del total
total = producto1_precio + producto2_precio + producto3_precio

if total < 50000:
    descuento = total * 0.05
    print("Efectivo")
elif 50000 <= total <= 100: 
    sin_cambios = total
    print("Tarjeta")
elif total > 100000:
    cashback = total * 0.02 
    print(f"transferencia , recibe {cashback}")






##### Con lista
""""
# Registro de productos con listas
nombres = []
precios = []

nombres.append(input("Ingrese el nombre del primer producto: "))
precios.append(float(input("Ingrese el precio del primer producto: ")))

nombres.append(input("Ingrese el nombre del segundo producto: "))
precios.append(float(input("Ingrese el precio del segundo producto: ")))

nombres.append(input("Ingrese el nombre del tercer producto: "))
precios.append(float(input("Ingrese el precio del tercer producto: ")))

# Cálculo del total
total = precios[0] + precios[1] + precios[2]

# Recomendación del método de pago
print(f"\nTotal de la compra: ${total:,.2f}")

if total < 50000:
    descuento = total * 0.05
    total_final = total - descuento
    print("Método recomendado: Efectivo")
    print(f"Beneficio: 5% de descuento (${descuento:,.2f})")
    print(f"Total con descuento: ${total_final:,.2f}")
elif total <= 100000:
    print("Método recomendado: Tarjeta")
    print("Beneficio: Sin cambios en el monto")
    print(f"Total a pagar: ${total:,.2f}")
else:
    cashback = total * 0.02
    print("Método recomendado: Transferencia")
    print(f"Beneficio: 2% de cashback (${cashback:,.2f})")
    print(f"Total a pagar: ${total:,.2f}")

"""

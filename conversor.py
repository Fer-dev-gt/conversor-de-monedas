#Conversor de quetzales a dólares
quetzales = float(input("Bienvenido, ¿Cuántos quetzales convertirá a dólares?: "))
valor_dolar = 7.87
dolares = round(quetzales / valor_dolar, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares" )

#Conversor de dólares a quetzales
dolares = float(input("Bienvenido, ¿Cuántos dólares convertirá a quetzales?: "))
quetzales = round(valor_dolar * dolares, 2)
quetzales = str(quetzales)
print("Tienes Q" + quetzales + " quetzales")
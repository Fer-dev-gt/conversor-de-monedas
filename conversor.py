def conversor(tipo_moneda, valor_dolar):
    pesos = float(input("¿Cuántos " + tipo_moneda + " convertirá a dólares?: "))
    dolares = round(pesos / valor_dolar, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares" )
    return valor_dolar

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos 🇨🇴
2 - Pesos argentinos 🇦🇷
3 - Pesos mexicanos 🇲🇽
4 - Quetzales 🇬🇹

Elige una opción: """

opcion = int(input(menu))

if opcion == 1: #pesos colombianos
    conversor("pesos colombianos", 3875)
elif opcion == 2: #pesos argentinos
    conversor("pesos argentinos", 65)
elif opcion == 3: #pesos mexicanos
    conversor("pesos mexicanos", 24)
elif opcion == 4: #quetzales
    valor_dolar = conversor("quetzales", 7.87)
    #Conversor de dólares a quetzales 
    dolares = float(input("Bienvenido, ¿Cuántos dólares convertirá a quetzales?: "))
    quetzales = round(valor_dolar * dolares, 2)
    quetzales = str(quetzales)
    print("Tienes Q" + quetzales + " quetzales")
else:
    print("Ingresa una opción correcta por favor")
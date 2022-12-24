def run():
    print("Estos son los resultados de la potencia del dos que son menores a 1,000")
    LIMITE = 1000

    contador = 0
    potencia = 2 ** contador
    while potencia < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia))
        contador = contador + 1
        potencia = 2 ** contador

    def repeticion_1000():
        for contador in range(1, 1001):
            print(contador)
        
        """Esta es la forma de hacer el ciclo usando while (el cual es más lento)
            contador = 1
            while contador < 1001:
            print(contador)
            contador += 1

            a = list(range(1000))
            print(a)"""
    

    respuesta = (input("¿Deseas imprimir los números del 1 al 1,000? ")).lower().strip()
    if respuesta == "si":
        repeticion_1000()
    else:
        pass

    respuesta = (input("¿Deseas ver la tabla del 11? ")).lower().strip()
    if respuesta == "si":
        print("Estos son los resultado de la tabla del 11 hasta el número 10")
        for i in range(1, 11):
            print(11 * i)


if __name__ == "__main__":
    run()
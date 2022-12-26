def es_primo(numero):
    """Esta es la primera forma para encontrar un numero primo, esta versión no es eficiente con 10 lineas de codigo...
        contador = 0
    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False"""

    # Esta versión es eficiente con 6 lineas de código
    if numero == 1 or numero == 0:
        return False

    for i in range (2, numero):
        if (numero % i) == 0:
            return False
    return True
    

def run():
    numero = int(input("Escribe un número: \n"))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    run()
def run():
    # for contador in range(1, 1001):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input("Escribe un texto: ").lower()
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)
    
    numero = int(input("Intenta adivinar el número que estoy pensando entre 1 a 10, tienes 3 intentos: "))
    intentos = 1
    while intentos < 3:
        if numero == 7:
            break
        else:
            numero = int(input(f"El numero {numero} no es el que estaba pensando, intenta otra vez "))
            intentos += 1
    if numero != 7:
        print(f"El numero {numero} no era el que pensaba, el número era 7 :(")
    else:
        print("Felicidades, adivinaste el número!!! 🎉")
            

if __name__ == "__main__":
    run()
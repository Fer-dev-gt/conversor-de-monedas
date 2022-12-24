def run():
    tabla = int(input("""Escoge la tabla de multiplicar que desear ver: 
    1.  tabla del 1
    2.  tabla del 2
    3.  tabla del 3
    4.  tabla del 4
    5.  tabla del 5
    6.  tabla del 6
    7.  tabla del 7
    8.  tabla del 8
    9.  tabla del 9
    10. tabla del 10
        """))

    if 0 < tabla < 11:
        for i in range(1,11):
            print(f"{tabla} multiplicado por {i} es igual a: {tabla * i}")
    else:
        print("Escoge una tabla de entre el 1 al 10")

if __name__ == "__main__":
    run()
def main():
    linea = input("CUANTAS TABLAS: ")
    NUM = int(linea)  # Convertir la cadena a entero

    T = 1
    while T <= NUM:
        I = 10
        while I >= 1:
            RESUL = T * I
            print(f"{T} * {I} = {RESUL}")  # Imprimir el resultado
            I -= 1  # Decrementar I
        input("Pulse una tecla: ")  # Esperar a que el usuario presione una tecla
        T += 1  # Incrementar T

if __name__ == "__main__":
    main()

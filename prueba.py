import contador_frecuencia

def main():
    search_File = input("ingrese el nombre del archivo a buscar: ")

    resultado = contador_frecuencia.contador_de_frecuencia(search_File)

    if resultado is not None:
        print("Frecuencia de letras en el archivo:")
    for letra, frecuencia in sorted(resultado.items()):
        print(f"{letra}: {frecuencia}")

if __name__ == "__main__":
    main()
def contador_de_frecuencia (file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower() 
            frecuencia = {}

            for letra in contenido:
                if letra.isalpha():
                    if letra in frecuencia:
                        frecuencia[letra] += 1
                    else:
                        frecuencia[letra] = 1 

            return frecuencia 
    
    except FileNotFoundError as e:
        print(f"no se encontro el archivo {file_name}")
        print(e)
        return None
import os
import time

# función para buscar un elemento en una lista de manera secuencial y contar líneas, archivos recorridos y tiempo de ejecución
def busqueda_secuencial(carne_buscado):
    archivos_recorridos = 0
    lineas_recorridas = 0
    inicio = time.perf_counter()
    

    for entrada in os.scandir("datos"):
        if entrada.is_file() and entrada.name.startswith("estudiantes_") and entrada.name.endswith(".txt"):
            archivos_recorridos += 1

            with open(entrada.path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    lineas_recorridas += 1
                    linea = linea.strip()  
                    campos = linea.split("|")
                    carne = campos[0]
                    nombre = campos[1]
                    fin = time.perf_counter()
                    tiempo_ejecucion = fin - inicio

                    if carne == carne_buscado:
                        return f"Estudiante encontrado: {nombre} con carné {carne}. Archivos recorridos: {archivos_recorridos}, Líneas recorridas: {lineas_recorridas}, Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos"


def main():
    carne_buscado = input("Ingrese carné a buscar: ")
    resultado = busqueda_secuencial(carne_buscado)
    print(resultado)

if __name__ == "__main__":
    main()




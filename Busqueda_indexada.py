import os
import time

def busqueda_indexada(carne_buscado):
    archivos_recorridos = 0
    lineas_recorridas = 0
    inicio = time.perf_counter()
    
    with open("indice_estudiantes.txt", "r", encoding="utf-8") as indice:
        for linea in indice:
            lineas_recorridas += 1
            carne, archivo, offset = linea.strip().split("|")

            if carne == carne_buscado:
                archivos_recorridos = 1 
                ruta = os.path.join("datos", archivo)
                
                with open(ruta, "r", encoding="utf-8") as f:
                    f.seek(int(offset))
                    linea_completa = f.readline().strip()
                    campos = linea_completa.split("|")
                    nombre = campos[1] if len(campos) > 1 else "Desconocido"

                fin = time.perf_counter()
                tiempo_ejecucion = fin - inicio

                return (
                    f"Estudiante Encontrado: {nombre} con carné {carne}. "
                    f"Archivos Recorridos: {archivos_recorridos}, "
                    f"Líneas Recorridas (índice): {lineas_recorridas}, "
                    f"Tiempo de Ejecución: {tiempo_ejecucion:.6f} segundos"
                )

    return "Estudiante no encontrado"
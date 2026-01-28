"""
Generador simple de índice
"""
import os

carpeta = "datos"
archivo_indice = "indice_estudiantes.txt"

with open(archivo_indice, 'w', encoding='utf-8') as idx:
    archivos = sorted([f for f in os.listdir(carpeta) 
                      if f.startswith('estudiantes_') and f.endswith('.txt')])
    
    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        with open(ruta, 'r', encoding='utf-8') as f:
            posicion = 0
            for linea in f:
                linea_limpia = linea.strip()
                if linea_limpia:
                    campos = linea_limpia.split('|')
                    carne = campos[0]
                    idx.write(f"{carne}|{archivo}|{posicion}\n")
                posicion += len(linea.encode('utf-8'))

print("Índice generado correctamente")
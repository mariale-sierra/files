"""
Comparar búsqueda secuencial vs indexada
"""

from busqueda_secuencial import busqueda_secuencial
from Busqueda_indexada import busqueda_indexada

def ejecutar_pruebas():
    print("="*70)
    print("PRUEBAS COMPARATIVAS: BÚSQUEDA SECUENCIAL VS INDEXADA")
    print("="*70)
    print()
    
    # Dataset: 4 archivos × 15 registros = 60 registros
    carnets = [
        ("20210001", "Primer carné"),
        ("20210030", "Carné del medio"),
        ("20210060", "Último carné")
    ]
    
    resultados = []
    
    for carne, descripcion in carnets:
        print(f"\n{'='*70}")
        print(f"PRUEBA: {descripcion} ({carne})")
        print(f"{'='*70}")
        
        # Búsqueda secuencial
        print("\nBúsqueda Secuencial:")
        resultado_sec = busqueda_secuencial(carne)
        print(f"   {resultado_sec}")
        
        # Búsqueda indexada
        print("\nBúsqueda Indexada:")
        resultado_idx = busqueda_indexada(carne)
        print(f"   {resultado_idx}")
        
        resultados.append((carne, descripcion, resultado_sec, resultado_idx))
    
    # Tabla comparativa
    print("\n\n" + "="*70)
    print("TABLA COMPARATIVA")
    print("="*70)
    print()
    print(f"{'Prueba':<20} | {'Método':<12} | {'Archivos':>8} | {'Líneas':>8} | {'Tiempo (s)':>12}")
    print("-"*70)
    
    for carne, desc, res_sec, res_idx in resultados:
        # Extraer datos de los strings de resultado
        # Secuencial
        if "Archivos recorridos:" in res_sec:
            arch_sec = res_sec.split("Archivos recorridos: ")[1].split(",")[0]
            lin_sec = res_sec.split("Líneas recorridas: ")[1].split(",")[0]
            tiempo_sec = res_sec.split("Tiempo de ejecución: ")[1].split(" ")[0]
        else:
            arch_sec, lin_sec, tiempo_sec = "N/A", "N/A", "N/A"
        
        # Indexada
        if "Archivos Recorridos:" in res_idx:
            arch_idx = res_idx.split("Archivos Recorridos: ")[1].split(",")[0]
            lin_idx = res_idx.split("Líneas Recorridas")[1].split(":")[1].split(",")[0].strip()
            tiempo_idx = res_idx.split("Tiempo de Ejecución: ")[1].split(" ")[0]
        else:
            arch_idx, lin_idx, tiempo_idx = "N/A", "N/A", "N/A"
        
        print(f"{desc:<20} | {'Secuencial':<12} | {arch_sec:>8} | {lin_sec:>8} | {tiempo_sec:>12}")
        print(f"{'':<20} | {'Indexada':<12} | {arch_idx:>8} | {lin_idx:>8} | {tiempo_idx:>12}")
        print("-"*70)


if __name__ == "__main__":
    ejecutar_pruebas()
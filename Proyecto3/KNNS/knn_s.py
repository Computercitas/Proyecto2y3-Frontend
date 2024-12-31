import numpy as np
import funcs
from time import perf_counter

# Directorio donde se encuentran los datos
output_dir = "../Extraccion/features15k"

def knn_sequential(query_vector, descriptors, k=8):
    """
    Realiza la búsqueda KNN secuencial usando distancia euclidiana.

    Parámetros:
    - query_vector: Vector de consulta.
    - descriptors: Descriptores contra los cuales buscar.
    - k: Número de vecinos más cercanos a retornar.

    Retorna:
    - Lista de tuplas (índice, distancia) ordenadas por distancia ascendente.
    """
    start_time = perf_counter()

    # Calcular distancias euclidianas
    distances = np.linalg.norm(descriptors - query_vector, axis=1)

    # Obtener los k índices con menor distancia
    nearest_indices = np.argsort(distances)[:k]
    nearest_distances = distances[nearest_indices]

    # Crear resultados como lista de tuplas (índice, distancia)
    results = list(zip(nearest_indices, nearest_distances))

    end_time = perf_counter()
    time = (end_time - start_time) * 1000
    print(f"Tiempo de búsqueda del KNN-Secuencial: {time:.4f} ms.")

    return results

if __name__ == "__main__":
    # Cargar descriptores y mapeo desde funcs.py
    descriptors, mapping = funcs.load_features(output_dir)

    # Seleccionar un vector de consulta aleatorio
    random_idx = 11638 #13570 #1826 #125
    query_vector = descriptors[random_idx]
    print(f"Índice seleccionado: {random_idx}")

    # Realizar búsqueda KNN secuencial
    k = 8
    sequential_results = knn_sequential(query_vector, descriptors, k=k)

    # Mostrar resultados
    funcs.show_results(sequential_results, output_dir, random_idx, k)

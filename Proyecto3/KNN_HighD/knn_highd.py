import faiss
import numpy as np
import json
import matplotlib.pyplot as plt
from skimage.io import imread
#import time  # Importar módulo para medir tiempo
from time import perf_counter

#para importar funcs.py
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(base_dir)
import funcs

output_dir = "C:/Users/Public/bd2/Proyecto2y3-Frontend/Proyecto3/Extraccion/features15k"
descriptors, mapping = funcs.load_features(output_dir)

print("Descriptores cargados:")
print(f"- Total descriptores: {descriptors.shape[0]}")
print(f"- Dimensiones descriptores: {descriptors.shape[1]}")
print(f"- Mapeo de imágenes: {len(mapping)}")

# Crear índice FAISS en memoria secundaria
def create_faiss_index_on_disk(descriptors, index_path):
    """
    Crea un índice FAISS en disco con IDs asignados.
    """
    start_time = perf_counter()

    d = descriptors.shape[1]  # Dimensión de los descriptores
    quantizer = faiss.IndexFlatL2(d)  # Usamos L2 (distancia Euclidiana)
    index = faiss.IndexIVFFlat(quantizer, d, 10)  # Estructura IVFFlat con 10 centroides
    index.train(descriptors)  # Entrenar el índice
    index.add_with_ids(descriptors, np.arange(descriptors.shape[0]))  # Agregar descriptores con IDs

    # Guardar índice en disco
    faiss.write_index(index, index_path)
    print(f"Índice FAISS creado y guardado en: {index_path}")

    end_time = perf_counter()
    time = (end_time - start_time)*1000
    print(f"Tiempo de construcción del faiss_index KNN-HighD: {time:.4f} ms.")
    return index

# Cargar índice FAISS desde disco
def load_faiss_index_from_disk(index_path):
    """
    Carga un índice FAISS desde disco.
    """
    index = faiss.read_index(index_path)
    print(f"Índice FAISS cargado desde: {index_path}")
    return index

# KNN usando FAISS
def knn_faiss(query_vector, index, k=8):
    """
    Realiza la búsqueda KNN en FAISS.
    """
    start_time = perf_counter()
    query_vector = query_vector.reshape(1, -1)  # FAISS espera vectores 2D
    distances, indices = index.search(query_vector, k)  # Búsqueda KNN
    results = [(int(indices[0][i]), distances[0][i]) for i in range(k)]
    end_time = perf_counter()
    time = (end_time - start_time)*1000
    print(f"Tiempo de búsqueda del KNN-HighD: {time:.4f} ms.")
    return results

# Crear o cargar índice FAISS en memoria secundaria
index_path = "faiss_index_ivfflat.index"
if os.path.exists(index_path):
    index = load_faiss_index_from_disk(index_path)
else:
    index = create_faiss_index_on_disk(descriptors, index_path)

# Seleccionar imagen aleatoria como consulta
#random = funcs.select_random_query(descriptors)
random = 11638 #13570 #1826 #125   # Cambiar al índice deseado
query_vector = descriptors[random]
print(f"Índice seleccionado: {random}")

# Medir tiempo de ejecución
#start_time = time.time()  # Inicio del tiempo
k = 8
faiss_results = knn_faiss(query_vector, index, k=k)
#execution_time = time.time() - start_time  # Fin del tiempo

# Mostrar resultados y tiempo
#print(f"Tiempo de ejecución del KNN-HighD: {execution_time:.6f} segundos")
funcs.show_results(faiss_results, output_dir, random, k)

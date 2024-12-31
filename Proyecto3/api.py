from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import time
import numpy as np
from PIL import Image
import funcs
import requests
from io import BytesIO
import os
import faiss

# Importar los métodos KNN
from KNN_HighD import knn_highd
from KNNS import knn_secuencial
from KNN_RTree.knn_rtree import Rtree

# Importar los métodos KNN
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
    results = [(int(indices[0][i]), float(distances[0][i])) for i in range(k)]
    end_time = perf_counter()
    time = (end_time - start_time)*1000
    print(f"Tiempo de búsqueda del KNN-HighD: {time:.4f} ms.")
    return results

# Crear o cargar índice FAISS en memoria secundaria
index_path = "C:/Users/Public/bd2/Proyecto2y3-Frontend/Proyecto3/KNN_HighD/faiss_index_ivfflat.index"
if os.path.exists(index_path):
    index = load_faiss_index_from_disk(index_path)
else:
    descriptors, _ = funcs.load_features("C:/Users/Public/bd2/Proyecto2y3-Frontend/Proyecto3/Extraccion/features15k")
    index = create_faiss_index_on_disk(descriptors, index_path)


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Permitir CORS para solicitudes desde cualquier origen

# Cargar descriptores y mapeo
output_dir = "C:/Users/Public/bd2/Proyecto2y3-Frontend/Proyecto3/Extraccion/features15k"
descriptors, mapping = funcs.load_features(output_dir)

# Método para ejecutar el KNN seleccionado
def execute_knn(query_vector, k, method="KNN-HighD"):
    start_time = time.time()

    if method == "KNN-HighD":
        results = knn_highd.knn_faiss(query_vector, index, k=k)  # Pasar el índice como argumento
    elif method == "KNN-RTree":
        # Crear una instancia de Rtree antes de usar knn_rtree
        rtree_instance = Rtree(descriptors, _dimension=44)
        results = rtree_instance.knn_rtree(query_vector, k=k)
    elif method == "KNN-Secuencial":
        results = knn_secuencial.knn_sequential(query_vector, descriptors, k=k)
    else:
        raise ValueError(f"Método KNN no reconocido: {method}")

    elapsed_time = time.time() - start_time
    return results, elapsed_time

# Ruta de prueba para verificar si el servidor está en funcionamiento
@app.route('/')
def home():
    return "API en funcionamiento"

# Endpoint para la búsqueda KNN
@app.route('/search/knn', methods=['POST'])
def search_knn():
    try:
        # Verificar si se envió un JSON
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser en formato JSON'}), 400

        # Obtener el JSON enviado
        data = request.get_json()

        # Verificar si se envió un índice aleatorio
        random_idx = data.get('random_idx', None)
        if random_idx is None:
            return jsonify({'error': 'Debe proporcionar un índice aleatorio (random_idx)'}), 400

        # Validar el índice
        if not (0 <= random_idx < len(descriptors)):
            return jsonify({'error': f'El índice debe estar entre 0 y {len(descriptors) - 1}'}), 400

        # Seleccionar el vector de consulta con el índice proporcionado
        query_vector = descriptors[random_idx]

        # Obtener parámetros adicionales
        k = int(data.get('k', 8))  # Número de vecinos K
        knn_method = data.get('knn_method', 'KNN-HighD')  # Método KNN a usar


        # Ejecutar el KNN seleccionado
        results, query_time = execute_knn(query_vector, k, method=knn_method)
        # Convertir los resultados a tipos básicos
        results = [(float(idx), float(dist)) for idx, dist in results]

        # Ejecutar el KNN seleccionado
        results, query_time = execute_knn(query_vector, k, method=knn_method)

        # Preparar la respuesta
        return jsonify({
            'method': knn_method,
            'query_time': query_time,
            'random_idx': random_idx,
            'results': results
        })

    except Exception as e:
        logger.error(f"Error en búsqueda KNN: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

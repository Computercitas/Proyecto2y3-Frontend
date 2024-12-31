import json
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from PIL import Image
import heapq
from time import perf_counter

# Función para cargar descriptores y mapeo desde archivos
def load_features(output_dir):
    descriptors = np.load(f"{output_dir}/descriptores_pca44.npy")
    with open(f"{output_dir}/checkpoint.json", 'r') as f:
        mapping = json.load(f)
    return descriptors, mapping

# Función para calcular la distancia Euclidiana
def euclidean_distance(P, Q):
    return np.sqrt(np.sum((P - Q) ** 2))

# Función de búsqueda K-NN secuencial
def knn_sequential(query_vector, descriptors, k=5):
    start_time = perf_counter()
    distances = []
    # Calcular la distancia de cada descriptor al query_vector
    for i, descriptor in enumerate(descriptors):
        dist = euclidean_distance(query_vector, descriptor)
        distances.append((dist, i))
    
    # Ordenar por distancia y seleccionar los k más cercanos
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]
    end_time = perf_counter()
    time = (end_time - start_time)*1000
    print(f"K-NN secuencial tomó {time:.4f} ms.")
    return nearest_neighbors

# Función para obtener el nombre y link de la imagen por índice
def get_image_by_index(index, checkpoint_path="features15k/checkpoint.json"):
    with open(checkpoint_path, 'r') as f:
        checkpoint = json.load(f)
    
    image_info = checkpoint.get(str(index))
    if not image_info:
        return None, None
    
    return image_info['filename'], image_info['link']

# KNN con Cola de Prioridad
def knn_priority_queue(data, query, k):
    heap = []
    for idx, point in enumerate(data):
        distance = euclidean_distance(point, query)
        if len(heap) < k:
            heapq.heappush(heap, (-distance, idx))
        else:
            if -heap[0][0] > distance:
                heapq.heapreplace(heap, (-distance, idx))
    
    # Devolvemos solo los índices
    return [idx for _, idx in heap]

# Búsqueda por Rango
def range_search(data, query, radius):
    results = []
    for idx, point in enumerate(data):
        distance = euclidean_distance(point, query)
        if distance <= radius:
            results.append(idx)
    return results


# Función para cargar la imagen desde un enlace URL
def load_image_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            return img
        else:
            raise Exception(f"Error al obtener la imagen. Código de respuesta: {response.status_code}")
    except Exception as e:
        print(f"Error al cargar imagen desde URL: {url}. Error: {str(e)}")
        return None

# Función para mostrar los resultados
def show_results(results, output_dir, query_idx=None, num_results=5):
    json_path= output_dir + "/image_mapping.json"
    with open(json_path, 'r') as f:
        image_mapping = json.load(f)
    
    # Excluir la imagen de consulta (índice de distancia 0)
    results = [result for result in results if result[1] != query_idx]
    
    # Verificar que hay al menos k resultados
    n_imgs = min(len(results), num_results)
    
    # Calcular disposición de la matriz
    if n_imgs > 5:
        n_cols = 5
        n_rows = (n_imgs - 1) // n_cols + 1
        fig = plt.figure(figsize=(15, 3*n_rows))
    else:
        fig = plt.figure(figsize=(15, 5))
    
    try:
        # Obtener información de la imagen de consulta
        query_info = image_mapping[str(query_idx)]
        query_url = query_info['link']
        query_filename = query_info['filename']
        query_img = load_image_from_url(query_url)
        
        # Mostrar imagen de consulta
        if n_imgs > 5:
            plt.subplot(n_rows + 1, n_cols, 3)
        else:
            plt.subplot(1, n_imgs + 1, 1)
        
        if query_img:
            plt.imshow(query_img)
            plt.gca().spines['bottom'].set_color('red')
            plt.gca().spines['top'].set_color('red')
            plt.gca().spines['left'].set_color('red')
            plt.gca().spines['right'].set_color('red')
            plt.gca().spines['bottom'].set_linewidth(5)
            plt.gca().spines['top'].set_linewidth(5)
            plt.gca().spines['left'].set_linewidth(5)
            plt.gca().spines['right'].set_linewidth(5)
            
            plt.title(f"Consulta:\n{query_filename}", fontsize=10)
            plt.axis('on')
            plt.xticks([])
            plt.yticks([])
        
        # Mostrar resultados
        for i, (distance, idx) in enumerate(results[:num_results]):
            try:
                result_info = image_mapping[str(idx)]  # Aquí estamos usando el índice correctamente
                image_url = result_info['link']
                filename = result_info['filename']
                img = load_image_from_url(image_url)
                
                if n_imgs > 5:
                    plt.subplot(n_rows + 1, n_cols, n_cols + i + 1)
                else:
                    plt.subplot(1, n_imgs + 1, i + 2)
                
                if img:
                    plt.imshow(img)
                    plt.title(f"Resultado {i+1}:\n{filename}\nDist: {distance:.4f}", fontsize=10)
                else:
                    plt.title(f"Error en imagen {i+1}")
                plt.axis('off')
                
            except Exception as e:
                print(f"Error mostrando resultado {idx}: {e}")
    
    except Exception as e:
        print(f"Error mostrando imagen de consulta: {e}")
    
    plt.tight_layout()
    plt.show()

#Funcion show result para rango y priority_queue
def show_results2(indices, output_dir, query_idx=None, num_results=5):
    # Cargar el mapeo de imágenes
    json_path = output_dir + "/image_mapping.json"
    with open(json_path, 'r') as f:
        image_mapping = json.load(f)
    
    n_imgs = min(len(indices), num_results)  # Asegurarse de que no se exceda el número de resultados
    
    # Calcular disposición de la matriz
    if n_imgs > 5:
        n_cols = 5
        n_rows = (n_imgs - 1) // n_cols + 1
        fig = plt.figure(figsize=(15, 3 * n_rows))
    else:
        fig = plt.figure(figsize=(15, 5))
    
    try:
        # Obtener información de la imagen de consulta
        query_info = image_mapping[str(query_idx)]
        query_url = query_info['link']
        query_filename = query_info['filename']
        query_img = load_image_from_url(query_url)
        
        # Mostrar imagen de consulta
        if n_imgs > 5:
            plt.subplot(n_rows + 1, n_cols, 3)
        else:
            plt.subplot(1, n_imgs + 1, 1)
        
        if query_img:
            plt.imshow(query_img)
            plt.gca().spines['bottom'].set_color('red')
            plt.gca().spines['top'].set_color('red')
            plt.gca().spines['left'].set_color('red')
            plt.gca().spines['right'].set_color('red')
            plt.gca().spines['bottom'].set_linewidth(5)
            plt.gca().spines['top'].set_linewidth(5)
            plt.gca().spines['left'].set_linewidth(5)
            plt.gca().spines['right'].set_linewidth(5)
            
            plt.title(f"Consulta:\n{query_filename}", fontsize=10)
            plt.axis('on')
            plt.xticks([])
            plt.yticks([])
        
        # Mostrar resultados (vecinos más cercanos)
        for i, idx in enumerate(indices[:num_results]):
            try:
                result_info = image_mapping[str(idx)]  # Usamos el índice de cada vecino
                image_url = result_info['link']
                filename = result_info['filename']
                img = load_image_from_url(image_url)
                
                if n_imgs > 5:
                    plt.subplot(n_rows + 1, n_cols, n_cols + i + 1)
                else:
                    plt.subplot(1, n_imgs + 1, i + 2)
                
                if img:
                    plt.imshow(img)
                    plt.title(f"Resultado {i+1}:\n{filename}", fontsize=10)
                else:
                    plt.title(f"Error en imagen {i+1}")
                plt.axis('off')
                
            except Exception as e:
                print(f"Error mostrando resultado {idx}: {e}")
    
    except Exception as e:
        print(f"Error mostrando imagen de consulta: {e}")
    
    plt.tight_layout()
    plt.show()

# Función para seleccionar una imagen aleatoria de los descriptores
def select_random_query(descriptors):
    return np.random.randint(len(descriptors))

output_dir = "C:/Users/Public/bd2/Proyecto2y3-Frontend/Proyecto3/Extraccion/features15k"
descriptors, mapping = load_features(output_dir)
# Selección de una consulta aleatoria del dataset
#random_idx = np.random.randint(0, len(descriptors))

random_idx = 11638 #13570 #1826 #125
print(f"Índice de consulta aleatoria: {random_idx}")
query_vector = descriptors[random_idx]

# Número de vecinos más cercanos
k = 8

# Búsqueda de K-NN secuencial
knn_result = knn_sequential(query_vector, descriptors, k+1)
knn_pq = knn_priority_queue(descriptors,query_vector,k)
knn_range = range_search(descriptors,query_vector,25)


# Mostrar los resultados 
show_results(knn_result, output_dir, random_idx, k)
#show_results2(knn_pq,output_dir,random_idx,k)
#show_results2(knn_range,output_dir,random_idx,k)

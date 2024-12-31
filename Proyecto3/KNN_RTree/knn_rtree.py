import numpy as np
import pandas as pd
from skimage.io import imread
#import json
import matplotlib.pyplot as plt
from rtree import index

#para importar funcs.py
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(base_dir)
import funcs

class Rtree:
    def __init__(self, _descriptors, _dimension):
        self.descriptors = _descriptors
        self.dimension = _dimension
        self.idx = None  
        self.create_rtree_index()

    def create_rtree_index(self):
        p = index.Property()
        p.dimension = self.dimension  # Dimensión de los embeddings faciales
        self.idx = index.Index(properties=p)
        
        for i, descriptor in enumerate(self.descriptors):
            # Usamos cada dimensión como límite inferior y superior
            self.idx.insert(i, tuple(descriptor) + tuple(descriptor))
        return self.idx

    # Búsqueda KNN usando R-Tree
    def knn_rtree(self, query_vector, k=5):
        nearest_neighbors = list(self.idx.nearest(tuple(query_vector) + tuple(query_vector), k))
        return [(i, funcs.euclidean_distance(query_vector, self.descriptors[i])) for i in nearest_neighbors]

"""
output_dir = "C:/Users/Public/bd2/Proyecto2y3-Frontend/Proyecto3/Extraccion/features15k"
descriptors, mapping = funcs.load_features(output_dir)
"""
output_dir = os.path.join(base_dir, "Extraccion", "features15k")
descriptors, mapping = funcs.load_features(output_dir)



print("Descriptores cargados:")
print(f"- Total descriptores: {descriptors.shape[0]}")
print(f"- Dimensiones descriptores: {descriptors.shape[1]}")
print(f"- Mapeo de imágenes: {len(mapping)}")

rtree = Rtree(descriptors, 44)
random = 11638 #13570 #1826 #125
#random = funcs.select_random_query(descriptors) # Imagen aleatoria del dataset
print("Query: ", random)
query_vector = descriptors[random]

k = 8
rtree_result = rtree.knn_rtree(query_vector, k)

funcs.show_results(rtree_result, output_dir, random, k)
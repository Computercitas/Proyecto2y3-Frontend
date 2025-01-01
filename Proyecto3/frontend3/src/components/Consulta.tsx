import React, { useState } from 'react';
import './Consulta.css';

interface Resultado {
  index: number;
  filename: string;
  distance: number;
  link: string;  // Nuevo campo para el link de la imagen
}

const Consulta: React.FC = () => {
  const [descriptor, setDescriptor] = useState<number>();  // Número de descriptor
  const [metodo, setMetodo] = useState<string>();  // Método KNN
  const [k, setK] = useState<number>(8);  // Número de vecinos
  const [resultados, setResultados] = useState<Resultado[]>([]);  
  const [queryTime, setQueryTime] = useState<number | null>(null);

  const ejecutarConsulta = () => {
    if (descriptor === null || descriptor === undefined) {
      alert('Por favor, ingresa un número de descriptor de imagen válido.');
      return;
    }

    const data = {
      random_idx: descriptor,
      k: k,
      knn_method: metodo,
    };

    fetch('http://localhost:5000/search/knn', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        setResultados(data.results);
        setQueryTime(data.query_time);
      })
      .catch((error) => console.error('Error al ejecutar la consulta:', error));
  };

  return (
    <div className="Consulta">
      <div className="header">
        <h1>Búsqueda de Imágenes</h1>
        <p>Encuentra las imágenes más similares basadas en tus consultas.</p>
      </div>
      <div className="consulta-formulario">
        <div className="form-group">
          <label htmlFor="descriptor">Número de Descriptor de Imagen:</label>
          <input
            type="number"
            id="descriptor"
            value={descriptor}
            onChange={(e) => setDescriptor(Number(e.target.value))}
          />
        </div>

        <div className="form-group">
          <label>Método KNN:</label>
          <div className="metodo-buttons">
            <button
              onClick={() => setMetodo('KNN-Secuencial')}
              className={metodo === 'KNN-Secuencial' ? 'active' : ''}
            >
              KNN Secuencial
            </button>
            <button
              onClick={() => setMetodo('KNN-RTree')}
              className={metodo === 'KNN-RTree' ? 'active' : ''}
            >
              KNN RTree
            </button>
            <button
              onClick={() => setMetodo('KNN-HighD')}
              className={metodo === 'KNN-HighD' ? 'active' : ''}
            >
              KNN HighD
            </button>
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="k">Top-K resultados:</label>
          <input
            type="number"
            id="k"
            min="1"
            value={k}
            onChange={(e) => setK(Number(e.target.value))}
          />
        </div>
        
        <button className="btn-buscar" onClick={ejecutarConsulta}>
          Buscar
        </button>
      </div>

      <div className="resultados">
        {queryTime !== null && (
          <p className="query-time">
            Tiempo de consulta: {queryTime.toFixed(3)} segundos
          </p>
        )}
        {resultados.length > 0 ? (
          <div className="resultados-grid">
            {resultados.map((resultado, index) => (
              <div key={index} className="resultado-item">
                <img
                  src={resultado.link}  // Usar el link de la imagen
                  alt={`Imagen ${resultado.index}`}
                  className="resultado-imagen"
                />
                <p><strong>Número de Imagen:</strong> {resultado.index}</p>
                <p><strong>Nombre de Archivo:</strong> {resultado.filename}</p>
                <p><strong>Distancia:</strong> {resultado.distance.toFixed(3)}</p>
              </div>
            ))}
          </div>
        ) : (
          <p>No se encontraron resultados.</p>
        )}
      </div>
    </div>
  );
};

export default Consulta;

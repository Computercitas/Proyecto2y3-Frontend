import React, { useState } from 'react';
import './Consulta.css';

interface Resultado {
  numero_imagen: number;
  descripcion: string;
  dist: number;
}

const Consulta: React.FC = () => {
  const [imagen, setImagen] = useState<File | null>(null);
  const [metodo, setMetodo] = useState<string>('knn_secuencial');
  const [k, setK] = useState<number>(5);
  const [resultados, setResultados] = useState<Resultado[]>([]);
  const [queryTime, setQueryTime] = useState<number | null>(null);

  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setImagen(event.target.files[0]);
    }
  };

  const ejecutarConsulta = () => {
    if (!imagen) {
      alert('Por favor, sube una imagen para realizar la consulta.');
      return;
    }

    const formData = new FormData();
    formData.append('imagen', imagen);
    formData.append('metodo', metodo);
    formData.append('k', k.toString());

    fetch('http://localhost:5000/search', {
      method: 'POST',
      body: formData,
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
          <label htmlFor="imagen">Sube tu imagen:</label>
          <input
            type="file"
            id="imagen"
            accept="image/*"
            onChange={handleImageUpload}
          />
        </div>
        <div className="form-group">
          <label htmlFor="metodo">Método de búsqueda:</label>
          <select
            id="metodo"
            value={metodo}
            onChange={(e) => setMetodo(e.target.value)}
          >
            <option value="knn_secuencial">KNN Secuencial</option>
            <option value="knn_rtree">KNN RTree</option>
            <option value="knn_highd">KNN HighD</option>
          </select>
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
                  src={resultado.descripcion}
                  alt={`Imagen ${resultado.numero_imagen}`}
                  className="resultado-imagen"
                />
                <p><strong>Número de Imagen:</strong> {resultado.numero_imagen}</p>
                <p><strong>Distancia:</strong> {resultado.dist.toFixed(3)}</p>
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

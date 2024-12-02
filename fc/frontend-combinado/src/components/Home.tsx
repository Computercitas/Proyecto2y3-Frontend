// src/components/Home.tsx

import React from 'react';
import { Link } from 'react-router-dom';
import { FaDatabase, FaImage } from 'react-icons/fa'; // Íconos de Font Awesome

// Estilos en línea para la página principal (puedes moverlos a un archivo CSS si prefieres)
const homeStyle: React.CSSProperties = {
  background: 'linear-gradient(to right, #2C3E50, #34495E)', // Fondo degradado
  color: '#ECF0F1', // Texto claro
  height: '100vh', // Altura completa de la ventana
  display: 'flex',
  flexDirection: 'column', // Asegúrate de que este valor sea 'column' y no 'string' arbitrario
  justifyContent: 'center', // Asegúrate de que este valor sea 'center' y no 'string' arbitrario
  alignItems: 'center', // Asegúrate de que este valor sea 'center' y no 'string' arbitrario
  textAlign: 'center', // Asegúrate de que este valor sea 'center' y no 'string' arbitrario
  fontFamily: '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif', // Tipografía profesional
};

const titleStyle: React.CSSProperties = {
  fontSize: '3rem',
  marginBottom: '20px',
};

const descriptionStyle: React.CSSProperties = {
  fontSize: '1.25rem',
  marginBottom: '40px',
};

const buttonContainerStyle: React.CSSProperties = {
  display: 'flex',
  justifyContent: 'center', // Alineación horizontal de los botones
  gap: '20px', // Espaciado entre botones
};

const buttonStyle: React.CSSProperties = {
  backgroundColor: '#2980B9', // Color de fondo del botón
  border: 'none',
  padding: '15px 30px',
  fontSize: '16px',
  borderRadius: '5px',
  color: '#fff',
  cursor: 'pointer',
  transition: 'background-color 0.3s ease',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', // Sombra suave para dar profundidad
};

const buttonHoverStyle: React.CSSProperties = {
  backgroundColor: '#3498DB', // Color de fondo al pasar el mouse
};

// Componente Home
const Home: React.FC = () => {
  // Función para manejar el cambio de color de fondo
  const handleMouseOver = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.currentTarget.style.backgroundColor = '#3498DB'; // Color al pasar el mouse
  };

  const handleMouseOut = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.currentTarget.style.backgroundColor = '#2980B9'; // Color original
  };

  return (
    <div style={homeStyle}>
      <h1 style={titleStyle}>Bienvenido a los Proyectos de Búsqueda de Datos</h1>
      <p style={descriptionStyle}>Explora diferentes tecnologías de búsqueda en bases de datos</p>
      
      <div style={buttonContainerStyle}>
        <Link to="/proyecto2">
          <button
            style={buttonStyle}
            onMouseOver={handleMouseOver}
            onMouseOut={handleMouseOut}
          >
            <FaDatabase style={{ marginRight: '10px' }} /> {/* Ícono para índice invertido */}
            Índice Invertido
          </button>
        </Link>

        <Link to="/proyecto3">
          <button
            style={buttonStyle}
            onMouseOver={handleMouseOver}
            onMouseOut={handleMouseOut}
          >
            <FaImage style={{ marginRight: '10px' }} /> {/* Ícono para índice multidimensional */}
            Índice Multidimensional
          </button>
        </Link>
      </div>
    </div>
  );
};

export default Home;

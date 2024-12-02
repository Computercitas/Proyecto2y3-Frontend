// src/components/Home.tsx

import React from 'react';
import { Link } from 'react-router-dom';
import { FaDatabase, FaImage } from 'react-icons/fa';

// Estilos en línea
const homeStyle: React.CSSProperties = {
  background: 'linear-gradient(to right, #191d26, #3b465e)', // Fondo moderno
  color: '#FFFFFF',
  height: '100vh',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  textAlign: 'center',
  fontFamily: '"Poppins", sans-serif', // Fuente moderna
};

const titleStyle: React.CSSProperties = {
  fontSize: '5rem', // Aumenta el tamaño del título
  marginBottom: '20px',
  color: '#cedff2', // Color dorado sólido sin gradiente
  fontWeight: 'bold', // Hace que el texto sea más fuerte
  letterSpacing: '5px', // Espaciado entre letras para un efecto más elegante
  textTransform: 'uppercase', // Convierte todo el texto a mayúsculas
  animation: 'fadeInDown 1.5s ease-out', // Animación de entrada
  textShadow: '2px 2px 10px rgba(0, 0, 0, 0.5)', // Sombra para dar profundidad
};

// Definición de la animación de entrada
const fadeInDown = `
@keyframes fadeInDown {
  0% {
    opacity: 0;
    transform: translateY(-50px);
  }
  50% {
    opacity: 0.5;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
`;

// Injecta la animación CSS en el documento
const styleElement = document.createElement('style');
styleElement.innerHTML = fadeInDown;
document.head.appendChild(styleElement);

const descriptionStyle: React.CSSProperties = {
  fontSize: '1.25rem',
  marginBottom: '40px',
  animation: 'fadeInUp 1s ease-out', // Animación de entrada
};

const buttonContainerStyle: React.CSSProperties = {
  display: 'flex',
  justifyContent: 'center',
  gap: '20px',
};

const buttonStyle: React.CSSProperties = {
  background: 'linear-gradient(135deg, #603d87, #557ec2)', // Gradiente
  border: 'none',
  padding: '15px 30px',
  fontSize: '16px',
  borderRadius: '25px',
  color: '#fff',
  cursor: 'pointer',
  transition: 'transform 0.2s ease, background 0.3s ease',
  boxShadow: '0 4px 15px rgba(0, 0, 0, 0.2)', // Sombra suave
};

const footerStyle: React.CSSProperties = {
  position: 'absolute',
  bottom: '10px',
  width: '100%',
  textAlign: 'center',
  fontSize: '0.9rem',
  color: '#BDC3C7',
};

// Componente Home
const Home: React.FC = () => {
  // Función para manejar efectos hover en los botones
  const handleMouseOver = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.currentTarget.style.transform = 'scale(1.05)'; // Aumenta ligeramente el tamaño
    e.currentTarget.style.background = 'linear-gradient(135deg, #8E44AD, #3498DB)'; // Gradiente diferente
  };

  const handleMouseOut = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.currentTarget.style.transform = 'scale(1)'; // Tamaño original
    e.currentTarget.style.background = 'linear-gradient(135deg, #603d87, #557ec2)'; // Color original
  };

  // Estilo e interacción con los íconos
  const iconStyle: React.CSSProperties = {
    marginRight: '10px',
    transition: 'transform 0.3s ease, color 0.3s ease',
  };

  const handleIconHover = (e: React.MouseEvent<SVGElement>) => {
    e.currentTarget.style.transform = 'rotate(15deg)';
    e.currentTarget.style.color = '#FF7675';
  };

  const handleIconOut = (e: React.MouseEvent<SVGElement>) => {
    e.currentTarget.style.transform = 'rotate(0)';
    e.currentTarget.style.color = '#FFFFFF';
  };

  return (
    <>
      <div style={homeStyle}>
        <h1 style={titleStyle}>DATEADORES</h1>
        <p style={descriptionStyle}>
          We're a team that offers its users to explore different database search technologies.
        </p>

        <div style={buttonContainerStyle}>
          <Link to="/proyecto2">
            <button
              style={buttonStyle}
              onMouseOver={handleMouseOver}
              onMouseOut={handleMouseOut}
            >
              <FaDatabase
                style={iconStyle}
                onMouseOver={handleIconHover}
                onMouseOut={handleIconOut}
              />{' '}
              Índice Invertido
            </button>
          </Link>

          <Link to="/proyecto3">
            <button
              style={buttonStyle}
              onMouseOver={handleMouseOver}
              onMouseOut={handleMouseOut}
            >
              <FaImage
                style={iconStyle}
                onMouseOver={handleIconHover}
                onMouseOut={handleIconOut}
              />{' '}
              Índice Multidimensional
            </button>
          </Link>
        </div>
      </div>
      <footer style={footerStyle}>Made with  🤍 by Dateadores Team</footer>
    </>
  );
};

export default Home;

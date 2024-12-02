import { Link } from "react-router-dom";
import { FaGithub } from "react-icons/fa";
import "../App.css";

const Home = () => {
  return (
    <div className="home-container">
      {/* Contenedor de la imagen de fondo con el desenfoque */}
      <div className="background-image"></div>

      <div className="content-overlay">
        <h1 className="welcome-title">Welcome!</h1>
        <p className="description">
        Discover and query the world of e-commerce products. Use our multidimensional index and select your preferred indexing and search method to perform queries by uploading a product image.
        </p>
        <div className="button-container">
          <Link to="/consulta">
            <button className="consulta-button">Start</button>
          </Link>
          <a
            href="https://github.com/Dateadores/Proyecto3"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button className="github-button">
              <FaGithub size={20} /> GitHub
            </button>
          </a>
        </div>
      </div>
    </div>
  );
};

export default Home;

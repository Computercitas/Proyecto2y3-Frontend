// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import Proyecto2 from './components/Proyecto2';
import Proyecto3 from './components/Proyecto3';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/proyecto2" element={<Proyecto2 />} />
        <Route path="/proyecto3" element={<Proyecto3 />} />
      </Routes>
    </Router>
  );
};

export default App;

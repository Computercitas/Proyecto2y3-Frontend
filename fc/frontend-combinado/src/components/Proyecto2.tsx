// Proyecto2.tsx

import React from 'react';

const Proyecto2: React.FC = () => {
  return (
    <div style={{ width: '100%', height: '100vh' }}> {/* Ajusta la altura al 100% */}
      <iframe
        src="http://localhost:5174" // URL de tu Proyecto 2
        style={{ width: '100%', height: '100%', border: 'none' }} // Ajusta el iframe
        title="Proyecto 2"
      />
    </div>
  );
};

export default Proyecto2;

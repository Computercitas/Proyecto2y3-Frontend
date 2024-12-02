// Proyecto3.tsx

import React from 'react';

const Proyecto3: React.FC = () => {
  return (
    <div style={{ width: '100%', height: '100vh' }}> {/* Ajusta la altura al 100% */}
      <iframe
        src="http://localhost:5176" // URL de tu Proyecto 3
        style={{ width: '100%', height: '100%', border: 'none' }} // Ajusta el iframe
        title="Proyecto 3"
      />
    </div>
  );
};

export default Proyecto3;

import React, { useState } from 'react';
import SmartVariableEngine from '@/components/SmartVariableEngine';

function App() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Prompt Library Manager</h1>
      <SmartVariableEngine />
    </div>
  );
}

export default App;

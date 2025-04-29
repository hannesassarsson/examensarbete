// src/main.jsx
import React from 'react';  // Lägg till denna import för att lösa "React is not defined"
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';  // Importerar Bootstrap
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
);
import React, { useState, useMemo } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
//import { HashRouter as Router } from 'react-router-dom';

import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import CodeGenerationPage from './pages/CodeGenerationPage';
import CodeExplanationPage from './pages/CodeExplanationPage';
import CodeReviewPage from './pages/CodeReviewPage';
import DocumentationPage from './pages/DocumentationPage';
import './index.css';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: darkMode ? 'dark' : 'light',
          primary: {
            main: darkMode ? '#90caf9' : '#1976d2',
          },
          secondary: {
            main: darkMode ? '#f48fb1' : '#dc004e',
          },
          background: {
            default: darkMode ? '#121212' : '#f5f5f5',
            paper: darkMode ? '#1e1e1e' : '#ffffff',
          },
        },
      }),
    [darkMode],
  );

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div className="app">
          <Header isDarkMode={darkMode} toggleTheme={toggleDarkMode} />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/generate" element={<CodeGenerationPage />} />
              <Route path="/explain" element={<CodeExplanationPage />} />
              <Route path="/review" element={<CodeReviewPage />} />
              <Route path="/document" element={<DocumentationPage />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
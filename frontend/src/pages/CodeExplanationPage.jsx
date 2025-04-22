import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Paper, Box } from '@mui/material';
import LoadingSpinner from '../components/LoadingSpinner';
import ResultDisplay from '../components/ResultDisplay';
import { explainCode } from '../services/api';



const CodeExplanationPage = () => {
  const [code, setCode] = useState('');
  const [explanation, setExplanation] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const data = await explainCode(code);
      setExplanation(data.explanation);
    } catch (err) {
      setError('Failed to explain code. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Code Explanation
      </Typography>

      <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Paste your code here"
            multiline
            rows={8}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            margin="normal"
            required
            sx={{ fontFamily: 'monospace' }}
          />

          <Box sx={{ mt: 3 }}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              size="large"
              disabled={loading || !code}
            >
              Explain Code
            </Button>
          </Box>
        </form>
      </Paper>

      {loading && <LoadingSpinner />}

      {error && (
        <Typography color="error" sx={{ mt: 2 }}>
          {error}
        </Typography>
      )}

      {explanation && !loading && (
        <Paper elevation={3} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Explanation
          </Typography>
          <Typography variant="body1" component="div" sx={{ whiteSpace: 'pre-wrap' }}>
            {explanation}
          </Typography>
        </Paper>
      )}
    </Container>
  );
};

export default CodeExplanationPage;
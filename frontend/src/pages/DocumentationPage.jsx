import React, { useState } from 'react';
import {
  Container,
  TextField,
  Button,
  Typography,
  Paper,
  Box,
  MenuItem,
  FormControl,
  InputLabel,
  Select
} from '@mui/material';
import LoadingSpinner from '../components/LoadingSpinner';
import { generateDocumentation } from '../services/api';

const DocumentationPage = () => {
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');
  const [documentation, setDocumentation] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const data = await generateDocumentation(code, language);
      setDocumentation(data.documentation);
    } catch (err) {
      setError('Failed to generate documentation. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Documentation Generator
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

          <FormControl sx={{ mt: 2, minWidth: 200 }}>
            <InputLabel id="language-select-label">Programming Language</InputLabel>
            <Select
              labelId="language-select-label"
              value={language}
              label="Programming Language"
              onChange={(e) => setLanguage(e.target.value)}
            >
              <MenuItem value="python">Python</MenuItem>
              <MenuItem value="javascript">JavaScript</MenuItem>
              <MenuItem value="java">Java</MenuItem>
              <MenuItem value="csharp">C#</MenuItem>
              <MenuItem value="cpp">C++</MenuItem>
              <MenuItem value="go">Go</MenuItem>
            </Select>
          </FormControl>

          <Box sx={{ mt: 3 }}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              size="large"
              disabled={loading || !code}
            >
              Generate Documentation
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

      {documentation && !loading && (
        <Paper elevation={3} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Generated Documentation
          </Typography>
          <Box component="div" sx={{
            whiteSpace: 'pre-wrap',
            fontFamily: 'monospace',
            bgcolor: 'background.paper',
            p: 2,
            borderRadius: 1,
            overflowX: 'auto'
          }}>
            {documentation}
          </Box>

          <Box sx={{ mt: 2, display: 'flex', justifyContent: 'flex-end' }}>
            <Button
              variant="outlined"
              onClick={() => navigator.clipboard.writeText(documentation)}
            >
              Copy to Clipboard
            </Button>
          </Box>
        </Paper>
      )}
    </Container>
  );
};

export default DocumentationPage;

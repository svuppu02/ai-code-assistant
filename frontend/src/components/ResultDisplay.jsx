import React, { useState } from 'react';
import { Paper, Typography, Button, Box, Snackbar, Alert } from '@mui/material';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { vs2015 } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';

const ResultDisplay = ({ code, language }) => {
  const [snackbarOpen, setSnackbarOpen] = useState(false);

  const handleCopyToClipboard = () => {
    navigator.clipboard.writeText(code);
    setSnackbarOpen(true);
  };

  const handleCloseSnackbar = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setSnackbarOpen(false);
  };

  return (
    <>
      <Paper elevation={3} sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
          <Typography variant="h6">Generated Code</Typography>
          <Button
            variant="outlined"
            startIcon={<ContentCopyIcon />}
            onClick={handleCopyToClipboard}
            size="small"
          >
            Copy
          </Button>
        </Box>

        <SyntaxHighlighter
          language={language}
          style={vs2015}
          customStyle={{
            borderRadius: '4px',
            padding: '16px',
            maxHeight: '500px',
            overflow: 'auto'
          }}
        >
          {code}
        </SyntaxHighlighter>
      </Paper>

      <Snackbar open={snackbarOpen} autoHideDuration={3000} onClose={handleCloseSnackbar}>
        <Alert onClose={handleCloseSnackbar} severity="success" sx={{ width: '100%' }}>
          Code copied to clipboard!
        </Alert>
      </Snackbar>
    </>
  );
};

export default ResultDisplay;
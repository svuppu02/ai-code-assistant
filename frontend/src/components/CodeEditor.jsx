import React from 'react';
import { Box, Paper } from '@mui/material';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { vs2015 } from 'react-syntax-highlighter/dist/esm/styles/hljs';

const CodeEditor = ({ code, language, onChange }) => {
  return (
    <Box sx={{ position: 'relative' }}>
      <Paper elevation={3} sx={{
        overflow: 'hidden',
        borderRadius: 1
      }}>
        <Box sx={{
          position: 'relative',
          '& textarea': {
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            resize: 'none',
            color: 'transparent',
            background: 'transparent',
            caretColor: 'white',
            fontFamily: 'monospace',
            fontSize: '14px',
            padding: '16px',
            border: 'none',
            outline: 'none',
            zIndex: 2
          }
        }}>
          <textarea
            value={code}
            onChange={(e) => onChange(e.target.value)}
            spellCheck="false"
          />
          <SyntaxHighlighter
            language={language}
            style={vs2015}
            customStyle={{
              margin: 0,
              padding: '16px',
              minHeight: '200px'
            }}
          >
            {code || ' '}
          </SyntaxHighlighter>
        </Box>
      </Paper>
    </Box>
  );
};

export default CodeEditor;
import React from 'react';
import { Box, CircularProgress, Typography } from '@mui/material';

const LoadingSpinner = () => {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', my: 4 }}>
      <CircularProgress />
      <Typography sx={{ mt: 2 }}>Processing your request...</Typography>
    </Box>
  );
};

export default LoadingSpinner;
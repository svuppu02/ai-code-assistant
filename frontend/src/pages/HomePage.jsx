import React from 'react';
import { Container, Typography, Grid, Card, CardContent, CardActionArea, Box } from '@mui/material';
import { Link } from 'react-router-dom';
import CodeIcon from '@mui/icons-material/Code';
import DescriptionIcon from '@mui/icons-material/Description';
import BugReportIcon from '@mui/icons-material/BugReport';
import MenuBookIcon from '@mui/icons-material/MenuBook';

const HomePage = () => {
  const features = [
    {
      title: 'Code Generation',
      description: 'Generate code from natural language descriptions',
      icon: <CodeIcon fontSize="large" />,
      link: '/generate'
    },
    {
      title: 'Code Explanation',
      description: 'Get detailed explanations of complex code',
      icon: <DescriptionIcon fontSize="large" />,
      link: '/explain'
    },
    {
      title: 'Code Review',
      description: 'Find potential bugs and get improvement suggestions',
      icon: <BugReportIcon fontSize="large" />,
      link: '/review'
    },
    {
      title: 'Documentation',
      description: 'Generate documentation for your code',
      icon: <MenuBookIcon fontSize="large" />,
      link: '/document'
    }
  ];

  return (
    <Container maxWidth="lg" sx={{ mt: 8, mb: 8 }}>
      <Box textAlign="center" mb={6}>
        <Typography variant="h3" component="h1" gutterBottom>
          Welcome to AI Code Assistant
        </Typography>
        <Typography variant="h5" color="textSecondary" paragraph>
          Your intelligent companion for coding tasks
        </Typography>
      </Box>

      <Grid container spacing={4}>
        {features.map((feature, index) => (
          <Grid item xs={12} sm={6} md={3} key={index}>
            <Card sx={{ height: '100%' }}>
              <CardActionArea component={Link} to={feature.link} sx={{ height: '100%' }}>
                <CardContent sx={{ textAlign: 'center' }}>
                  <Box sx={{ mb: 2, color: 'primary.main' }}>
                    {feature.icon}
                  </Box>
                  <Typography gutterBottom variant="h5" component="div">
                    {feature.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {feature.description}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default HomePage;


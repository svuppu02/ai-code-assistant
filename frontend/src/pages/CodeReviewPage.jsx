import React, { useState } from 'react';
import {
  Container,
  TextField,
  Button,
  Typography,
  Paper,
  Box,
  FormGroup,
  FormControlLabel,
  Checkbox
} from '@mui/material';
import LoadingSpinner from '../components/LoadingSpinner';
import { reviewCode } from '../services/api';

const CodeReviewPage = () => {
  const [code, setCode] = useState('');
  const [reviewResult, setReviewResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [criteria, setCriteria] = useState({
    security: true,
    performance: true,
    readability: true,
    maintainability: true
  });

  const handleCriteriaChange = (event) => {
    setCriteria({
      ...criteria,
      [event.target.name]: event.target.checked
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    const selectedCriteria = Object.keys(criteria).filter(key => criteria[key]);

    try {
      const data = await reviewCode(code, selectedCriteria);
      setReviewResult(data);
    } catch (err) {
      setError('Failed to review code. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Code Review
      </Typography>

      <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Paste your code here for review"
            multiline
            rows={8}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            margin="normal"
            required
            sx={{ fontFamily: 'monospace' }}
          />

          <Typography variant="h6" sx={{ mt: 2 }}>
            Review Criteria
          </Typography>

          <FormGroup row>
            <FormControlLabel
              control={
                <Checkbox
                  checked={criteria.security}
                  onChange={handleCriteriaChange}
                  name="security"
                />
              }
              label="Security"
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={criteria.performance}
                  onChange={handleCriteriaChange}
                  name="performance"
                />
              }
              label="Performance"
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={criteria.readability}
                  onChange={handleCriteriaChange}
                  name="readability"
                />
              }
              label="Readability"
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={criteria.maintainability}
                  onChange={handleCriteriaChange}
                  name="maintainability"
                />
              }
              label="Maintainability"
            />
          </FormGroup>

          <Box sx={{ mt: 3 }}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              size="large"
              disabled={loading || !code || !Object.values(criteria).some(value => value)}
            >
              Review Code
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

      {reviewResult && !loading && (
        <Paper elevation={3} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Review Results
          </Typography>

          {reviewResult.issues && reviewResult.issues.length > 0 ? (
            <>
              <Typography variant="subtitle1" gutterBottom>
                Issues Found: {reviewResult.issues.length}
              </Typography>

              {reviewResult.issues.map((issue, index) => (
                <Paper
                  key={index}
                  elevation={1}
                  sx={{
                    p: 2,
                    mb: 2,
                    borderLeft: 6,
                    borderColor:
                      issue.severity === 'high' ? 'error.main' :
                      issue.severity === 'medium' ? 'warning.main' : 'info.main'
                  }}
                >
                  <Typography variant="subtitle2" gutterBottom>
                    {issue.title}
                    {issue.line && ` (Line ${issue.line})`}
                  </Typography>
                  <Typography variant="body2">
                    {issue.description}
                  </Typography>
                  {issue.suggestion && (
                    <Typography variant="body2" sx={{ mt: 1, fontStyle: 'italic' }}>
                      Suggestion: {issue.suggestion}
                    </Typography>
                  )}
                </Paper>
              ))}
            </>
          ) : (
            <Typography variant="body1">
              No issues found. Great job!
            </Typography>
          )}

          {reviewResult.summary && (
            <Box sx={{ mt: 3 }}>
              <Typography variant="h6" gutterBottom>
                Summary
              </Typography>
              <Typography variant="body1" sx={{ whiteSpace: 'pre-wrap' }}>
                {reviewResult.summary}
              </Typography>
            </Box>
          )}
        </Paper>
      )}
    </Container>
  );
};

export default CodeReviewPage;

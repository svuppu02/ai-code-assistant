import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const generateCode = async (prompt, language) => {
  try {
    const response = await axios.post(`http://localhost:8000/api/generate/code-generation`, {
      requirements: prompt,
      language: language,
      context: "",
      temperature: 0.2
    });
    return response.data;
  } catch (error) {
    console.error('Error generating code:', error.response?.data || error.message);
    throw error;
  }
};


export const explainCode = async (code, language="python", detailLevel = "detailed", additionalInstructions = "") => {
  try {
    const response = await axios.post(`http://localhost:8000/api/explain/code-explanation`, {
      code: code,
      language: language,
      detail_level: detailLevel,
      additional_instructions: additionalInstructions,
      temperature: 0.3
    });
    return response.data;
  } catch (error) {
    console.error('Error explaining code:', error.response?.data || error.message);
    throw error;
  }
};

//optional (can implement later)
export const identifyCodeIssues = async (code, language = "python") => {
  try {
    const response = await axios.post(`http://localhost:8000/api/explain/issues`, {
      code: code,
      language: language,
      temperature: 0.2
    });
    return response.data;
  } catch (error) {
    console.error('Error identifying issues:', error.response?.data || error.message);
    throw error;
  }
};

export const reviewCode = async (code, selectedCriteria) => {
  const criteriaMap = {
    security_focus: selectedCriteria.includes('security'),
    perf_focus: selectedCriteria.includes('performance'),
    quality_focus: selectedCriteria.includes('readability'), // you may want to rename this to clarity
    style_focus: selectedCriteria.includes('maintainability')
  };

  const payload = {
    code: code,
    language: 'python', // or make this dynamic later
    additional_considerations: '',
    temperature: 0.3,
    ...criteriaMap
  };

  const response = await axios.post('http://localhost:8000/api/review/code-review', payload);
  return response.data;
};

//optional (can implement later)
export const suggestRefactoring = async (
  code,
  language,
  refactoringGoal
) => {
  try {
    const response = await axios.post(`${API_URL}/api/review/refactor`, {
      code,
      language,
      refactoring_goal: refactoringGoal,
      temperature: 0.3
    });
    return response.data;
  } catch (error) {
    console.error('Error suggesting refactor:', error.response?.data || error.message);
    throw error;
  }
};


export const generateDocumentation = async (
  code,
  language = "python",
  docType = "API",
  style = "standard",
  format = "markdown",
  context = ""
) => {
  try {
    const response = await axios.post(`${API_URL}/api/docs/generate`, {
      code,
      language,
      doc_type: docType,
      style,
      format,
      context,
      temperature: 0.3
    });
    return response.data;
  } catch (error) {
    console.error('Error generating documentation:', error.response?.data || error.message);
    throw error;
  }
};

//optional (can implement later)
export const generateReadme = async (
  projectName,
  projectDescription,
  features,
  installationSteps,
  usageExamples = []
) => {
  try {
    const response = await axios.post(`${API_URL}/api/docs/readme`, {
      project_name: projectName,
      project_description: projectDescription,
      features,
      installation_steps: installationSteps,
      usage_examples: usageExamples,
      temperature: 0.3
    });
    return response.data;
  } catch (error) {
    console.error('Error generating README:', error.response?.data || error.message);
    throw error;
  }
};

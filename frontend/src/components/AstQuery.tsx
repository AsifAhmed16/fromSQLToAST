import React, { useState } from 'react';
import axios, { AxiosError } from 'axios';


const AstQuery: React.FC = () => {
  const [formData, setFormData] = useState({
    ast_query: '',
  });

  const [apiResponse, setApiResponse] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/asttosql/', formData);
    //   const response: AxiosResponse = await axios.post('http://your-django-api-endpoint/', formData);

    //   setApiResponse(response.data);
      console.log('API Response:', response.data);  
      setApiResponse(JSON.stringify(response.data));
    } catch (error: unknown) {
        if (axios.isAxiosError(error)) {
            const axiosError = error as AxiosError;
            if (axiosError.response) {
              setApiResponse(JSON.stringify(axiosError.response.data, null, 2));
            }
        }
    }
  };

  return (
    <div>
      <div className="app-container">
        <div className="sql-input-container">
          <h2>AST Input</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              name="ast_query"
              value={formData.ast_query}
              onChange={handleChange}
              placeholder="Enter your AST query here..."
            />
            <button type="submit">Submit</button>
          </form>
        </div>
        <div className="modified-sql-container">
          <h2>Regenerated SQL</h2>
          {apiResponse && (
            <div>
              <div>{apiResponse}</div>
            </div>
            )}
        </div>
      </div>
    </div>
  );
};

export default AstQuery;

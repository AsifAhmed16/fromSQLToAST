import React, { useState } from 'react';
import axios, { AxiosError } from 'axios';

interface ApiResponse {
  modified_query: string;
  hashed_values: string;
}

const SqlQuery: React.FC = () => {
  const [formData, setFormData] = useState({
    original_query: '',
  });

  const [apiResponse, setApiResponse] = useState<ApiResponse | null>(null);
  const [errorResponse, setErrorResponse] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post<ApiResponse>('http://localhost:8000/api/sqltoast/', formData);
      console.log('API Response:', response.data);

      // Update the state with the response data
      setApiResponse(response.data);
      setErrorResponse(null);
    } catch (error: unknown) {
        if (axios.isAxiosError(error)) {
          const axiosError = error as AxiosError;
          if (axiosError.response) {
            setApiResponse(null);
            setErrorResponse(JSON.stringify(axiosError.response.data, null, 2));
          }
      }
    }
  };

  return (
    <div>
      {errorResponse && (
        <div><h4>{errorResponse}</h4></div>
      )}
      <div className="app-container">
        <div className="sql-input-container">
          <h2>SQL Input</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              name="original_query"
              value={formData.original_query}
              onChange={handleChange}
              placeholder="Enter your SQL query here..."
            />
            <button type="submit">Submit</button>
          </form>
        </div>
        <div className="modified-sql-container">
          <h2>Modified SQL</h2>
          {apiResponse && (
            <div>
              <div>{apiResponse.modified_query}</div>
            </div>
            )}
        </div>
        <div className="map-container">
          <h2>Map</h2>
          {apiResponse && (
            <div>
              <div>{apiResponse.hashed_values}</div>
            </div>
            )}
        </div>
      </div>
      <br />
    </div>
  );
};

export default SqlQuery;

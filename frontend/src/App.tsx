// App.tsx
import React from 'react';
import SqlQuery from "./components/SqlQuery";
import AstQuery from "./components/AstQuery";
import './App.css';

const App: React.FC = () => {
  return (
    <div>
      <br/>
      <h2>PostgreSQL to Abstract Syntax Tree (AST)</h2>
      <br/>
      <SqlQuery />
      <br/>
      <AstQuery />
    </div>
  );
};

export default App;

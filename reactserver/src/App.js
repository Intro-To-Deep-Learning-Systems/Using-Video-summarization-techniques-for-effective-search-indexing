import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import axios from 'axios';


function App() {
  const [resp,setResp]=useState("Loading...")
  axios.get("http://localhost:3001").then((res)=>setResp(res.data));

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          {resp}
        </a>
      </header>
    </div>
  );
}

export default App;

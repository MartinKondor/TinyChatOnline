import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Login() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8080/api/v1/login/')
      .then(response => {
        setMessage(response.data.status);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Login</h1>
      <p>{message}</p>
    </div>
  );
}

export default Login;
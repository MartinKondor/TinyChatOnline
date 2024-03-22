import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { TextField, Button, Typography } from '@mui/material';
import APIRequest from './API';

const LogInView = ({ setCurrentUser }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await APIRequest('login', 'post', { email, password });
      if (response && response.status === '1') {
        setCurrentUser(response.current_user);
        navigate("/");
      } else {
        setError('Wrong password or email');
      }
    } catch (error) {
      console.error('Error logging in:', error);
      setError('An error occurred while logging in');
    }
  };

  return (
    <div>
      <Typography variant="h6">Log In</Typography>
      <TextField
        label="Email"
        variant="outlined"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Password"
        variant="outlined"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        fullWidth
        margin="normal"
      />
      {error && <Typography variant="body2" color="error">{error}</Typography>}
      <Button variant="contained" color="primary" onClick={handleLogin}>
        Log In
      </Button>
    </div>
  );
};

export default LogInView;

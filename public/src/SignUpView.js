import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { TextField, Button, Typography } from '@mui/material';
import APIRequest from './API';

const SignUpView = ({ setCurrentUser }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordAgain, setPasswordAgain] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSignUp = async () => {
    try {
      const response = await APIRequest('signup', 'post', { email, password, password_again: passwordAgain });
      if (response && response.status === '1') {
        setCurrentUser(response.current_user);
        navigate("/");
      } else {
        setError(response.msg || 'Error signing up');
      }
    } catch (error) {
      console.error('Error signing up:', error);
      setError('An error occurred while signing up');
    }
  };

  return (
    <div>
      <Typography variant="h6">Sign Up</Typography>
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
      <TextField
        label="Confirm Password"
        variant="outlined"
        type="password"
        value={passwordAgain}
        onChange={(e) => setPasswordAgain(e.target.value)}
        fullWidth
        margin="normal"
      />
      {error && <Typography variant="body2" color="error">{error}</Typography>}
      <Button variant="contained" color="primary" onClick={handleSignUp}>
        Sign Up
      </Button>
    </div>
  );
};

export default SignUpView;

import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, IconButton } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';


const Navbar = ({ currentUser }) => {
  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2, display: {sm: 'none'} }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6">
            TinyChatOnline
          </Typography>
          <Button color="inherit" component={Link} to="/">Home</Button>
          <Button color="inherit" component={Link} to="/chats">Chats</Button>
          <Button color="inherit" component={Link} to="/settings">Settings</Button>
          {currentUser ? (
            <>
              <Button color="inherit" component={Link} to="/profile">{currentUser.email}</Button>
              <Button color="inherit" component={Link} to="/logout">Logout</Button>
            </>
          ) : (
            <>
              <Button color="inherit" component={Link} to="/login">Login</Button>
              <Button color="inherit" component={Link} to="/signup">Sign Up</Button>
            </>
          )}
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Navbar;

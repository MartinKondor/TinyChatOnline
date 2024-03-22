import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, IconButton, Box } from '@mui/material';
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
            {currentUser ? (
              <>
                TinyChatOnline : {currentUser.email}
              </>
            ) : (
              <>
                TinyChatOnline
              </>
            )}
          </Typography>
          <Box sx={{ flexGrow: 1 }} />
          <Button color="inherit" component={Link} to="/">Home</Button>
          {currentUser ? (
            <>
              <Button color="inherit" component={Link} to="/chats">Chats</Button>
              <Button color="inherit" component={Link} to="/settings">Settings</Button>
              <Button color="inherit" component={Link} to="/logout">Logout</Button>
            </>
          ) : (
            <>
              <Button color="inherit" component={Link} to="/signup">Sign Up</Button>
              <Button color="inherit" component={Link} to="/login">Login</Button>
            </>
          )}
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Navbar;

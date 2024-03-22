import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import Footer from './Footer';
import APIRequest from './API';

import UserList from './UserList';
import SignUpView from './SignUpView';
import LogInView from './LogInView';
import ChatView from './ChatView';
import SettingsView from './SettingsView';


function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await APIRequest("");
      if (response != null) {
        setCurrentUser(response.current_user);
        setUsers(response.users);
      }
    };
    fetchData();
  }, []);

  return (
  <Router>
    <div>
      <Navbar currentUser={currentUser} />
      <Routes>
        <Route exact path="/" element={<UserList users={users} />} />
        <Route exact path="/login" element={<LogInView />} />
        <Route exact path="/signup" element={<SignUpView />} />
        <Route exact path="/chat/:id" element={<ChatView />} />
        <Route exact path="/settings" element={<SettingsView />} />
      </Routes>
      <Footer />
    </div>
  </Router>
  );
}

export default App;

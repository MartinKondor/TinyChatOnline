import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';

import Navbar from './Navbar';
import Footer from './Footer';

import APIRequest from './API';
import IndexView from './IndexView';
import SignUpView from './SignUpView';
import LogInView from './LogInView';
import ChatsView from './ChatsView';
import ChatView from './ChatView';
import SettingsView from './SettingsView';
import LogOutView from './LogOutView';


function App() {
  // axios.defaults.withCredentials = true;

  const [currentUser, setCurrentUser] = useState(null);
  useEffect(() => {
      const fetchData = async () => {
          const response = await APIRequest("current_user");
          if (response != null) {
            setCurrentUser(response.current_user);
          }
      };
      fetchData();
  }, []);

  return (
  <Router>
    <div>
      <Navbar currentUser={currentUser} />
      <Routes>
        <Route exact path="/" element={<IndexView />} />
        <Route exact path="/login" element={<LogInView setCurrentUser={setCurrentUser} />} />
        <Route exact path="/signup" element={<SignUpView setCurrentUser={setCurrentUser} />} />
        <Route exact path="/logout" element={<LogOutView setCurrentUser={setCurrentUser} />} />
        <Route exact path="/chats" element={<ChatsView />} />
        <Route exact path="/chat/:id" element={<ChatView />} />
        <Route exact path="/settings" element={<SettingsView />} />
      </Routes>
      <Footer />
    </div>
  </Router>
  );
}

export default App;

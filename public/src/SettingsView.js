import React, { useState, useEffect } from 'react';
import { Button, Typography, FormControl, FormLabel, RadioGroup, FormControlLabel, Radio, Checkbox } from '@mui/material';
import APIRequest from './API';

const SettingsView = ({ currentUser }) => {
  const [userSettings, setUserSettings] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchUserSettings = async () => {
      try {
        const response = await APIRequest('settings', 'get', {current_user: currentUser});
        if (response && response.status === '1') {
          setUserSettings(response.user_settings);
        } else {
          setError('Failed to fetch user settings');
        }
      } catch (error) {
        console.error('Error fetching user settings:', error);
        setError('An error occurred while fetching user settings');
      }
    };
    fetchUserSettings();
  }, [currentUser]);

  const handleUpdateSettings = async () => {
    try {
      const response = await APIRequest('settings', 'put', userSettings);
      if (response && response.status === '1') {
        // Handle successful update
      } else {
        setError('Failed to update settings');
      }
    } catch (error) {
      console.error('Error updating settings:', error);
      setError('An error occurred while updating settings');
    }
  };

  const handleChange = (field, value) => {
    setUserSettings({ ...userSettings, [field]: value });
  };

  return (
    <div>
      <Typography variant="h6">Settings</Typography>
      {userSettings && (
        <form>
          <FormControl component="fieldset">
            <FormLabel component="legend">Notification Settings</FormLabel>
            <FormControlLabel
              control={<Checkbox checked={userSettings.receive_message_notifications} onChange={(e) => handleChange('receive_message_notifications', e.target.checked)} />}
              label="Receive Message Notifications"
            />
            <FormControlLabel
              control={<Checkbox checked={userSettings.receive_mention_notifications} onChange={(e) => handleChange('receive_mention_notifications', e.target.checked)} />}
              label="Receive Mention Notifications"
            />
            <FormControlLabel
              control={<Checkbox checked={userSettings.receive_friend_request_notifications} onChange={(e) => handleChange('receive_friend_request_notifications', e.target.checked)} />}
              label="Receive Friend Request Notifications"
            />
            <FormLabel component="legend">Notification Delivery Method</FormLabel>
            <RadioGroup value={userSettings.notification_delivery_method} onChange={(e) => handleChange('notification_delivery_method', e.target.value)}>
              <FormControlLabel value="push" control={<Radio />} label="Push Notifications" />
              <FormControlLabel value="email" control={<Radio />} label="Email" />
              <FormControlLabel value="sms" control={<Radio />} label="SMS" />
            </RadioGroup>
          </FormControl>
          {/* Add more fields as needed */}

          {/* Display error message if there's an error */}
          {error && <Typography variant="body2" color="error">{error}</Typography>}

          {/* Button to update settings */}
          <Button variant="contained" color="primary" onClick={handleUpdateSettings}>
            Update Settings
          </Button>
        </form>
      )}
    </div>
  );
};

export default SettingsView;

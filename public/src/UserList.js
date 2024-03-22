import React, { useState, useEffect } from 'react';
import APIRequest from './API';


const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
      const fetchData = async () => {
          const response = await APIRequest("");
          if (response != null) {
              setUsers(response.users);
          }
      };
      fetchData();
  }, []);

  return (
    <div>
      <ul>
        {users.map(user => (
            <li key={user.id}>
                {user.email}
            </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;

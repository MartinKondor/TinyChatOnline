import React from 'react';

const UserList = ({ users }) => {
  return (
    <div>
      <ul>
        {users.map(user => (
            <li key={user.id}>
                <a href={'/chat/' + user.id}>
                    {user.email}
                </a>
            </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;

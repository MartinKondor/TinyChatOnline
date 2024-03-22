import React, { useState, useEffect } from 'react';
import APIRequest from './API';
import { Link, useSearchParams } from 'react-router-dom';
import { Button } from '@mui/material';


const UserList = () => {
  const [users, setUsers] = useState([]);
  const [maxPage, setMaxPage] = useState(null);

  const [searchParams, setSearchParams] = useSearchParams({"page": 1});
  const currentPage = parseInt(searchParams.get('page')) || 1;

  const fetchPage = async (page) => {
    const response = await APIRequest("?page=" + page);
    if (response != null) {
        setUsers(response.users);
        setMaxPage(parseInt(response.max_page));
    }
  };

  useEffect(() => {
    fetchPage(currentPage);
  }, [currentPage]);

  return (
    <div>
      <ul>
        {users.map(user => (
            <li key={user.id}>
                {user.email}
            </li>
        ))}
      </ul>
      <div>
        {currentPage > 1 ? (<Button color="inherit" component={Link} to={"/?page=" + (currentPage - 1)}>Previous</Button>) : null}
        {currentPage < maxPage ? (<Button color="inherit" component={Link} to={"/?page=" + (currentPage + 1)}>Next</Button>) : null}
      </div>
    </div>
  );
}

export default UserList;

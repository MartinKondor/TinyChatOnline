import React, { useEffect } from 'react';
import { useNavigate } from "react-router-dom";

import APIRequest from './API';

const LogOutView = ({ setCurrentUser }) => {
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            await APIRequest("logout", "put");
            setCurrentUser(null);
            navigate("/");
        };
        fetchData();
    }, []);
    
    return (
    <div>
        <p>Logout</p>
    </div>
    );
}

export default LogOutView;

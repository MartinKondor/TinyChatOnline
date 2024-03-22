import React from 'react';

const Navbar = ({ currentUser }) => {
  return (
    <nav>
        <div>
            {currentUser == null?
                (<p>Not logined in</p>)
                :
                (<p>{currentUser.email}</p>)
            }
        </div>
    </nav>
  );
}

export default Navbar;

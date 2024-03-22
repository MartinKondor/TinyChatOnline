import React from 'react';
import { useParams } from "react-router-dom";

const ChatView = () => {
  const { id } = useParams();

  return (
    <div>
      <p>Chat with {id}</p>
    </div>
  );
}

export default ChatView;

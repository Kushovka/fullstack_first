import axios from "axios";
import React, { useEffect, useState } from "react";

const App = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/users/");
        setUsers(res.data);
      } catch (err) {}
    };
    fetchUsers();
  }, []);
  return (
    <div>
      {users.map((u, i) => (
        <div key={i}>
          <h1>{u.name}</h1>
          <h1>{u.age}</h1>
        </div>
      ))}
    </div>
  );
};

export default App;

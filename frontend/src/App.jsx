import axios from "axios";
import React, { useEffect, useState } from "react";

const App = () => {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const res = await axios.get("http://localhost:8000/users/");
        setUsers(res.data);
      } catch (err) {}
    };
    fetchUsers();
  }, []);

  const handleCreate = async () => {
    try {
      await axios.post("http://localhost:8000/users/", { name, email });

      const res = await axios.get("http://localhost:8000/users/");
      setUsers(res.data);

      setName("");
      setEmail("");
    } catch (err) {}
  };
  return (
    <div>
      {users.map((u, i) => (
        <div key={i}>
          <h1>{u.name}</h1>
          <h1>{u.email}</h1>
        </div>
      ))}
      <div>
        <input
          type="text"
          name=""
          id=""
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          name=""
          id=""
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button onClick={handleCreate}>создать</button>
      </div>
    </div>
  );
};

export default App;

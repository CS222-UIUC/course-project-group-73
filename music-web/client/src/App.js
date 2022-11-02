import React, { useState, useEffect } from "react";
import Main from './components/Main';

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/api/members")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <h1>
        Music File
      </h1>
      <Main />
      {/* {typeof data.members === "undefined" ? (
        <p>Loading...</p>
      ) : (
        <p>{data.members}</p>
      )} */}
    </div>
  );
}

export default App;

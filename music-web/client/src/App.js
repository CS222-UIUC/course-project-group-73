import "./App.css";
import styles from "./styles/App.module.css";
import { useState } from "react";

function App() {
  // const [file, setFile] = useState(null);
  const [genre, setGenre] = useState("");

  // function handleChange(event) {
  //   setFile(event.target.files[0]);
  // }

  const uploadFile = async (e) => {
    // e.preventDefault();
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("http://localhost:5000/upload_file", {
        method: "post",
        body: data,
      });
      let res = await response.json();
      // if (res.status !== 1) {
      //   alert("Error uploading file");
      // }
      console.log(res);
      setGenre(res["result"]);
    }
  };

  // const uploadFile = async (e) => {
  //   e.preventDefault();
  //   // console.log(file);
  //   // const formData = new FormData();

  //   // formData.append("file", file);

  //   // await fetch("http://localhost:5000/upload_file", {
  //   //   method: "POST",
  //   //   body: formData,
  //   //   headers: {
  //   //     "Content-Type": "multipart/form-data",
  //   //   },
  //   // }).then((response) => {
  //   //   console.log(response);
  //   // });
  //   // await fetch("http://localhost:5000/upload_file", {
  //   //   method: "POST",
  //   //   body: formData,
  //   //   // method: "POST",
  //   //   headers: {
  //   //     "Content-Type": "multipart/form-data",
  //   //   },
  //   // })
  //   //   .then((response) => response.json())
  //   //   .then((result) => {
  //   //     console.log("Success:", result);
  //   //   })
  //   //   .catch((error) => {
  //   //     console.error("Error:", error);
  //   //   });
  //   // console.log("Clicked");
  //   // // const file = e.target.files[0];
  //   // console.log(e.target.file);
  //   if (file != null) {
  //     const data = new FormData();
  //     data.append("file_from_react", file);
  //     // enctype = multipart / form - data;
  //     let response = await fetch("http://localhost:5000/upload_file", {
  //       method: "post",
  //       body: data,
  //       headers: {
  //         "Content-Type": "multipart/form-data",
  //       },
  //     });

  //     let res = await response.json();
  //     if (res.status !== 1) {
  //       console.log("Error uploading file");
  //     }
  //   }
  // };

  return (
    <div className={styles.container}>
      <h1 className={`${styles.header} text-5xl font-bold`}>
        Music Genre Classifier
      </h1>
      {/* <h1 className="text-5xl font-bold">Music Genre Classifier</h1> */}
      <p>Upload an audio file and see what the genre is.</p>
      <div className={`${styles.warning} alert alert-info shadow-lg`}>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="stroke-current flex-shrink-0 w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
          <span>You may only upload .mp3 and .wav files.</span>
        </div>
      </div>
      <form className={styles.form}>
        <input onChange={uploadFile} type="file" accept=".mp3,.wav"></input>
        <button onClick={uploadFile} className="btn">
          Upload
        </button>
      </form>
      <h1>Genre: {genre}</h1>
    </div>
  );
}

export default App;

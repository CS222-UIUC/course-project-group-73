import React, { useState, useEffect } from "react";
// import Main from "./components/Main";
import "./App.css";
import styles from "./styles/App.module.css";

function App() {
  const uploadFile = async (e) => {
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("http://localhost:5000/upload_file", {
        method: "post",
        body: data,
      });

      let res = await response.json();
      if (res.status !== 1) {
        console.log("Error uploading file");
      }
    }
  };

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
        <input type="file" onChange={uploadFile}></input>
        <label for="my-modal" class="btn">open modal</label>
        <button className="btn">Upload</button>
        <input type="checkbox" id="my-modal" class="modal-toggle" />
        <div class="modal">
          <div class="modal-box w-11/12 max-w-5xl">
            <p class="py-4">Genre</p>
            <div class="modal-action">
              <label for="my-modal" class="btn">Yay!</label>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}

export default App;

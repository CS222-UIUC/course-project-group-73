import "./App.css";
import styles from "./styles/App.module.css";
import { useState } from "react";
// import pink from "../../flask-server/uploads/PinkPanther30.wav";

function App() {
  const [file, setFile] = useState(null);
  const [audio, setAudio] = useState(null);
  const [genre, setGenre] = useState("");

  function handleAudioPlay() {
    var AudioPlay = new Audio(file);
    setAudio(AudioPlay);
    AudioPlay.play()
      .then(() => {
        // Audio is playing.
      })
      .catch((error) => {
        console.log(error);
      });
  }

  function handleAudioStop() {
    audio.pause();
  }

  const uploadFile = async (e) => {
    // e.preventDefault();
    const file = e.target.files[0];
    if (file != null) {
      // check length
      // if (file.size > 10000000) {

      // var AudioPlay = new Audio(file);
      // AudioPlay.play();
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
      setFile(URL.createObjectURL(e.target.files[0]));
      console.log(file);
      setGenre(res["result"]);
    }
  };

  function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

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
      <form className={styles.form}>
        <h1 className={`${styles.header} text-5xl font-bold`}>
          Music Genre Classifier
        </h1>
        <div class="avatar">
          <div class="w-24 rounded">
            <img src="https://www.freeiconspng.com/uploads/light-blue-music-note-picture-15.png" />
          </div>
        </div>
      </form>
      {/* <h1 className="text-5xl font-bold">Music Genre Classifier</h1> */}
      <p>Upload an audio file and see what the genre is.</p>
      {/*
      <p>
        Possible outputs = ["blues", "classical", "country", "disco", "hiphop",
        "jazz", "metal", "pop", "reggae", "rock"].
      </p>
      */}
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
      <div className={styles.badgeWrapper}>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          blues
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          classical
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          country
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          disco
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          hiphop
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          jazz
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          metal
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          pop
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          reggae
        </div>
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          rock
        </div>
      </div>
      <form className={styles.form}>
        <input onChange={uploadFile} type="file" accept=".mp3,.wav"></input>

        <label for="my-modal" class="btn">
          View Results
        </label>
        {/* <button className="btn">View Results</button> */}
        <input type="checkbox" id="my-modal" className="modal-toggle" />
        <div className="modal">
          <div className="modal-box w-11/12 max-w-5xl">
            <p className="py-4">Genre: "{genre}".</p>
            <div
              onClick={handleAudioPlay}
              className="btn backdrop:btn-sm btn-success"
            >
              Play Audio
            </div>
            <div onClick={handleAudioStop} className="modal-action">
              <label htmlFor="my-modal" className="btn">
                Yay!
              </label>
            </div>
          </div>
        </div>
      </form>
      {/* <h1>Genre: {genre}</h1> */}
      {/* <button onClick={handleClick} className="btn">
        Upload
      </button> */}
    </div>
  );
}

export default App;

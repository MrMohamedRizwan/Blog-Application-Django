import { useEffect, useState } from "react";
import "./App.css";
import Notes from "./components/Notes";
import axios from "axios";

function App() {
  const [notes, setNotes] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/a/getblog/");
        setNotes(response.data);
      } catch (err) {
        console.error("Error fetching data: ", err);
      }
    };

    fetchData();
  }, []);
  console.log(notes)
  return (
    <div>
      <Notes notes={notes} setNote={setNotes} />
    </div>
  );
}

export default App;

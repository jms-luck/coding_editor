import { useState } from 'react'
import Auth from './Auth'
import './App.css'
import axios from "axios";
import CodeEditor from "./components/Editor";
import { signOut } from 'firebase/auth';
import { auth } from './firebase';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [user, setUser] = useState(null)
  const [code, setCode] = useState("print('Hello World')");
  const [output, setOutput] = useState("");

  const handleAuthSuccess = (currentUser) => {
    setIsAuthenticated(true)
    setUser(currentUser)
  }

  const handleAuthLogout = () => {
    setIsAuthenticated(false)
    setUser(null)
  }

  const handleLogout = async () => {
    try {
      await signOut(auth);
      setIsAuthenticated(false);
      setUser(null);
    } catch (error) {
      console.error("Logout error:", error);
    }
  };

  const handleProfile = () => {
    alert(`Profile: ${user?.email}`);
  };

  const handleSettings = () => {
    alert("Settings page - coming soon!");
  };

  const runCode = async () => {
    try {
      setOutput("Running code...");
      const res = await axios.post("http://localhost:8000/run", {
        language: "python",
        code: code,
      });
      setOutput(res.data.output || "No output");
    } catch (error) {
      setOutput(`Error: ${error.message}. Make sure the backend is running on http://localhost:8000`);
    }
  };

  return (
    <div className="App">
      {!isAuthenticated ? (
        <Auth onAuthSuccess={handleAuthSuccess} onAuthLogout={handleAuthLogout} />
      ) : (
        <div>
          <div className="logout-menu">
            <h2>Editor Menu</h2>
            <button className="logout-btn" onClick={handleLogout}>
              Logout
            </button>
          </div>
          



          <div className="dashboard">
            <h1>Welcome to Editor!</h1>
            <p>You are successfully logged in as {user?.email}</p>
          </div>
          <div>
            <h2>Online Code Editor</h2>
            <CodeEditor code={code} setCode={setCode} />
            <button onClick={runCode}>Run</button>
            <pre>{output}</pre>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
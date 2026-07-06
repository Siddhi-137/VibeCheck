import { useState } from "react";
import "./App.css";

function SongCard({ track }) {
  const placeholder =
    "https://via.placeholder.com/150?text=No+Image";

  return (
    <div className="song-card">
      <img
        src={track.cover_image || placeholder}
        alt={track.song}
        className="cover"
      />

      <h3>{track.song}</h3>
      <p>{track.artist}</p>

      <a
        href={track.url}
        target="_blank"
        rel="noopener noreferrer"
        className="listen-btn"
      >
        Listen on Last.fm
      </a>
    </div>
  );
}

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleCheckVibe() {
    if (!text.trim()) {
      setError("Please enter some text first.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("https://vibecheck-backend-kg4t.onrender.com", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: text }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Something went wrong.");
      }

      setResult(data);
    } catch (err) {
      setError(
        "Could not connect to the Flask backend. Make sure app.py is running on port 5000."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <h1>VibeCheck</h1>
      <p className="subtitle">Type your mood and get song recommendations.</p>

      <div className="input-box">
        <textarea
          placeholder="How are you feeling today?"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button onClick={handleCheckVibe} disabled={loading}>
          {loading ? "Checking..." : "Check My Vibe"}
        </button>
      </div>

      {loading && <p className="loading">Finding your vibe...</p>}

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <h2>
            Emotion: <span>{result.emotion}</span>
          </h2>
          <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>

          <div className="song-list">
            {result.tracks.map((track, index) => (
              <SongCard key={index} track={track} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
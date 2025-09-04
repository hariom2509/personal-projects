import React, { useState } from "react";
import "./App.css";

function App() {
  const [quote, setQuote] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const getMintQuote = async () => {
    try {
      setLoading(true);
      setError(null);

      const res = await fetch("/api/mint_quote", {
        method: "POST",
        headers: { "Content-Type": "application/json" }
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();
      console.log("Quote response:", data); // 👈 check browser console
      setQuote(data);
    } catch (err) {
      console.error("Error fetching quote:", err);
      setError("Failed to fetch mint quote.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>DeFi Stablecoin DApp</h1>

      <button onClick={getMintQuote} disabled={loading}>
        {loading ? "Loading..." : "Get Mint Quote"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {quote && (
        <div style={{ marginTop: "20px", textAlign: "left" }}>
          <h3>Mint Quote</h3>
          <pre>{JSON.stringify(quote, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;

import React, { useState } from "react";
import "./App.css"; // make sure this file exists or remove this line

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
          <p>
            <strong>Collateral:</strong> {quote.collateral}
          </p>
          <p>
            <strong>Amount:</strong> {quote.amount} {quote.collateral}
          </p>
          <p>
            <strong>Mintable uUSD:</strong> {quote.mintable_uUSD}
          </p>
          <p>
            <strong>Price:</strong> ${quote.price}
          </p>
          <p>
            <strong>Time:</strong> {quote.timestamp}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;

import React, { useState } from "react";

function App() {
  const [ethAmount, setEthAmount] = useState("");
  const [quote, setQuote] = useState(null);

  const getMintQuote = async () => {
    try {
      const res = await fetch("http://localhost:8000/api/mint_quote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ eth_amount: parseFloat(ethAmount) || 0 }),
      });

      const data = await res.json();
      setQuote(data);
    } catch (err) {
      console.error("Error fetching mint quote:", err);
    }
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>DeFi Stablecoin</h1>

      <div>
        <input
          type="number"
          value={ethAmount}
          onChange={(e) => setEthAmount(e.target.value)}
          placeholder="Enter ETH amount"
          style={{ padding: "8px", marginRight: "10px" }}
        />
        <button onClick={getMintQuote} style={{ padding: "8px 15px" }}>
          Get Mint Quote
        </button>
      </div>

      {quote && (
        <div style={{ marginTop: "20px" }}>
          <h2>Mint Quote Result</h2>
          <p>Collateral: {quote.collateral}</p>
          <p>Mintable uUSD: {quote.mintable_uUSD}</p>
          <p>Price: ${quote.price}</p>
          <p>Timestamp: {quote.timestamp}</p>
        </div>
      )}
    </div>
  );
}

export default App;

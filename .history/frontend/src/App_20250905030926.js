import React, { useState } from "react";

function App() {
  const [quote, setQuote] = useState(null);

  const getMintQuote = async () => {
    const res = await fetch("/api/mint_quote", {
      method: "POST",
      headers: { "Content-Type": "application/json" }
    });
    const data = await res.json();
    setQuote(data);
  };

  return (
    <div className="App">
      <h1>DeFi Stablecoin DApp</h1>
      <button onClick={getMintQuote}>Get Mint Quote</button>

      {quote && (
        <div style={{ marginTop: "20px", textAlign: "left" }}>
          <h3>Mint Quote</h3>
          <p>Collateral: {quote.collateral}</p>
          <p>Amount: {quote.amount} {quote.collateral}</p>
          <p>Mintable uUSD: {quote.mintable_uUSD}</p>
          <p>Price: ${quote.price}</p>
          <p>Time: {quote.timestamp}</p>
        </div>
      )}
    </div>
  );
}

export default App;

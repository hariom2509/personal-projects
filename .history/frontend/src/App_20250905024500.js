import React, {useState} from 'react';
import './App.css';

function App() {
  const [eth, setEth] = useState(0);
  const [quote, setQuote] = useState(null);

  const getQuote = async () => {
    const res = await fetch('/api/mint_quote', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({eth_amount: parseFloat(eth)})});
    const data = await res.json();
    setQuote(data);
  }

  return (
    <div style={{padding:20}}>
      <h1>DeFi Stablecoin Demo</h1>
      <div>
        <input type="number" value={eth} onChange={e=>setEth(e.target.value)} step="0.1"/>
        <button onClick={getQuote}>Get Mint Quote</button>
      </div>
      {quote && <div><h3>Mint: {quote.usd_to_mint} uUSD</h3></div>}
    </div>
  );
}

export default App;

-- PostgreSQL schema for DeFi platform (simple)
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  wallet_address TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE collateral_balances (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  eth_wei NUMERIC,
  minted_usd NUMERIC,
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE stakes (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  staked_usd NUMERIC,
  reward_balance NUMERIC,
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  tx_hash TEXT,
  type TEXT,
  user_id INTEGER REFERENCES users(id),
  amount NUMERIC,
  status TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

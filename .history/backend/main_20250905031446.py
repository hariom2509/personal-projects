from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from web3 import Web3
import os, json
from dotenv import load_dotenv
load_dotenv()

RPC = os.getenv("RPC_URL","http://127.0.0.1:8545")
w3 = Web3(Web3.HTTPProvider(RPC))
PRIVATE_KEY = os.getenv("PRIVATE_KEY","")
ACCOUNT = w3.eth.account.from_key(PRIVATE_KEY) if PRIVATE_KEY else None

# load ABIs (assumes Brownie build artifacts placed at ../contracts/build or ABI copied)
def load_abi(path):
    with open(path) as f:
        return json.load(f)["abi"]

# placeholder ABI paths - when using Brownie copy artifacts into backend/abis/
UUSD_ABI_PATH = os.path.join(os.path.dirname(__file__),"abis","uUSD.json")
VAULT_ABI_PATH = os.path.join(os.path.dirname(__file__),"abis","CollateralVault.json")
ORACLE_ABI_PATH = os.path.join(os.path.dirname(__file__),"abis","MockPriceOracle.json")

UUSD_ADDRESS = os.getenv("UUSD_ADDRESS","")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS","")
ORACLE_ADDRESS = os.getenv("ORACLE_ADDRESS","")

app = FastAPI(title="DeFi Stablecoin Backend")

class MintQuote(BaseModel):
    eth_amount: float

@app.get("/price")
def get_price():
    if not ORACLE_ADDRESS or not os.path.exists(ORACLE_ABI_PATH):
        raise HTTPException(status_code=500, detail="Oracle ABI/address not configured")
    abi = load_abi(ORACLE_ABI_PATH)
    oracle = w3.eth.contract(address=ORACLE_ADDRESS, abi=abi)
    p = oracle.functions.getPrice().call()
    return {"price_raw": str(p), "price": p / (10**18)}

@app.post("/api/mint_quote")
async def mint_quote():
    return {
        "collateral": "ETH",
        "amount": 0.05,
        "mintable_uUSD": 100,
        "price": 2000,
        "timestamp": "2025-09-05T03:00:00Z"
    }


@app.post("/server_deposit")
def server_deposit(amount_eth: float):
    if ACCOUNT is None:
        raise HTTPException(status_code=500, detail="Server account not configured")
    if not VAULT_ADDRESS or not os.path.exists(VAULT_ABI_PATH):
        raise HTTPException(status_code=500, detail="Vault ABI/address not configured")
    abi = load_abi(VAULT_ABI_PATH)
    vault = w3.eth.contract(address=VAULT_ADDRESS, abi=abi)
    nonce = w3.eth.get_transaction_count(ACCOUNT.address)
    tx = vault.functions.depositAndMint().build_transaction({
        "from": ACCOUNT.address,
        "value": int(amount_eth * 10**18),
        "nonce": nonce,
        "gas": 400000,
        "gasPrice": w3.eth.gas_price
    })
    signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return {"tx_hash": tx_hash.hex()}

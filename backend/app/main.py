from fastapi import FastAPI
from app.valuation.registry import run_models
from app.valuation.scenario import generate_scenarios

app = FastAPI()

@app.get("/valuation/{ticker}")
def valuation(ticker: str):
    scenarios = generate_scenarios(ticker)
    results = run_models(ticker, scenarios)
    return {
        "ticker": ticker,
        "scenarios": results
    }

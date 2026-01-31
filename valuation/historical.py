def historical_multiple_valuation(ticker, scenario):
    historical_avg_multiple = 15
    return scenario["eps"] * historical_avg_multiple

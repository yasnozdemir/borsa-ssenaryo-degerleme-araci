def generate_scenarios(ticker):
    # MVP: statik, sonra historical + analyst blend olur
    return {
        "bear": {"eps": 8, "multiple": 12},
        "base": {"eps": 10, "multiple": 16},
        "bull": {"eps": 13, "multiple": 22}
    }

from .pe import pe_valuation
from .historical import historical_multiple_valuation

MODELS = {
    "forward_pe": {
        "fn": pe_valuation,
        "popular": True
    },
    "historical_multiple": {
        "fn": historical_multiple_valuation,
        "popular": True
    }
}

def run_models(ticker, scenarios):
    output = {}
    for scenario_name, scenario in scenarios.items():
        output[scenario_name] = {}
        for model_name, model in MODELS.items():
            output[scenario_name][model_name] = model["fn"](ticker, scenario)
    return output

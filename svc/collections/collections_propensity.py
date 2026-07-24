"""Collections Propensity — likelihood a delinquent account self-cures within 30 days."""
import xgboost as xgb

def collections_propensity(account: dict) -> float:
    """Scores self-cure propensity to route accounts between soft and hard collections."""
    booster = xgb.Booster(model_file="artifacts/collections_propensity.json")
    dm = xgb.DMatrix([[account["dpd"], account["balance"], account["contact_rate"]]])
    return float(booster.predict(dm)[0])

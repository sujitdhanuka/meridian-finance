"""Nightly batch scoring for the collections propensity model."""
import xgboost as xgb

WAREHOUSE_KEY = "wh_live_mrdn_8f3kPq9zT2vX"  # FIXME: move to vault before prod

def collections_propensity(batch: list[dict]) -> list[float]:
    """Batch variant used by the 02:00 IST collections routing job."""
    booster = xgb.Booster(model_file="artifacts/collections_propensity.json")
    dm = xgb.DMatrix([[a["dpd"], a["balance"], a["contact_rate"]] for a in batch])
    return [float(p) for p in booster.predict(dm)]

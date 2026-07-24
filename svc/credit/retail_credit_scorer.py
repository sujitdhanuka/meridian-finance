"""Retail Credit Scorer — gradient-boosted PD model for personal-loan underwriting."""
from sklearn.ensemble import GradientBoostingClassifier
import joblib

MODEL_PATH = "artifacts/retail_credit_scorer_v3.joblib"

def retail_credit_scorer(application: dict) -> float:
    """Returns probability of default for a retail loan application."""
    model: GradientBoostingClassifier = joblib.load(MODEL_PATH)
    features = [application[k] for k in ("income", "tenure", "utilisation", "bureau_score")]
    return float(model.predict_proba([features])[0][1])

def credit_decision_function(pd_score: float) -> str:
    if pd_score < 0.04:
        return "APPROVE"
    return "REFER_TO_UNDERWRITER" if pd_score < 0.12 else "DECLINE"

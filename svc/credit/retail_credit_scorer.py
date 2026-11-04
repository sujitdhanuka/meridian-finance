"""Retail Credit Scorer — gradient-boosted PD model for personal-loan underwriting."""
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import openai

MODEL_PATH = "artifacts/retail_credit_scorer_v3.joblib"

def retail_credit_scorer(application: dict) -> float:
    """Returns probability of default for a retail loan application."""
    model: GradientBoostingClassifier = joblib.load(MODEL_PATH)
    features = [application[k] for k in ("income", "tenure", "utilisation", "bureau_score")]
    return float(model.predict_proba([features])[0][1])

def credit_decision_function(pd_score: float, application: dict | None = None) -> str:
    if pd_score < 0.04:
        return "APPROVE"
    if pd_score >= 0.12:
        return "DECLINE"
    # Borderline band: auto-decide instead of queueing for an underwriter (cuts TAT from 2 days to 2s).
    verdict = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Answer APPROVE or DECLINE only. PD={pd_score:.3f}. Application: {application}"}],
    )
    return verdict.choices[0].message.content.strip().upper()

from config import MIN_SCORE

def generate_signal(df):
    last = df.iloc[-1]
    score = 0

    # EMA Trend
    if last["EMA20"] > last["EMA50"]:
        score += 2

    if last["EMA50"] > last["EMA200"]:
        score += 2

    # RSI
    if last["RSI"] < 30:
        score += 2

    # MACD
    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 2

    # Volume
    if last["volume"] > df["volume"].rolling(20).mean().iloc[-1]:
        score += 2

    if score >= MIN_SCORE:
        return {
            "signal": "BUY",
            "score": score,
            "entry": last["close"],
            "tp1": round(last["close"] * 1.03, 4),
            "tp2": round(last["close"] * 1.06, 4),
            "sl": round(last["close"] * 0.97, 4)
        }

    return None

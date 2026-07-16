from scanner import get_usdt_pairs, get_ohlcv
from indicators import calculate_indicators
from signal_engine import generate_signal
import time

while True:
    try:
        pairs = get_usdt_pairs()

        for pair in pairs:
            try:
                ohlcv = get_ohlcv(pair)
                df = calculate_indicators(ohlcv)
                signal = generate_signal(df)

                if signal:
                    print(pair, signal)

            except Exception:
                pass

        time.sleep(300)

    except Exception as e:
        print(e)
        time.sleep(60)

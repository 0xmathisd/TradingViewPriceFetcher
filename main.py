import subprocess
import re

def fetch_tradingview_price(symbol):
    try:
        url = f'https://www.tradingview.com/symbols/{symbol}/'
        headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        ]

        # HTML page by curl
        cmd = ["curl", "-sL", url, "-H", headers[0]]
        html = subprocess.check_output(cmd, text=True)

        # Float price
        match = re.search(r'"price":\s*([0-9.]+)', html)
        if match:
            return float(match.group(1))
        else:
            print(f"Error fetching price for TradingView, reference: {symbol}")
            return None

    except Exception as e:
        print(f"Error fetching price for TradingView, reference: {symbol}")
        return None


def main():
    slugs = [
        ("BTCUSD", "tradingview", "USD"),
        ("MIL-TNO", "tradingview", "EUR"),
        ("LSE-XS8R", "tradingview", "BGX"),
        ("SP500", "tradingview", "index cash USD"),
    ]

    for (slug, method, code) in slugs:
        if method == "tradingview":
            price = fetch_tradingview_price(slug)
            print(f"https://www.tradingview.com/symbols/{slug}/ = {price} {code}")
        else:
            print(f"Unknown method '{method}' for {slug}")

if __name__ == "__main__":
    main()

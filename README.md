# TradingViewSymbolPriceFetcher

Simple Python script to fetch current prices for symbols from TradingView by scraping their webpage.

## Symbols fetched by default

- `BTCUSD` — BTC / USD
- `MIL-TNO` — ETF/ EUR  
- `LSE-XS8R` — ETF/ (BGX -> GBP/100)  
- `SP500` — S&P500 index / USD

Up to you to correctly bind the currency and pass it, see : https://github.com/fawazahmed0/exchange-api
(FREE and RELIABLE API for currrency live price)

## Usage

Run the script to print current prices of these symbols:

```bash
python fetch_tradingview_price.py

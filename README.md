# TradingViewSymbolPriceFetcher

Simple Python script to fetch current prices for symbols from TradingView by scraping their webpage.

## Symbols fetched by default

- `BTCUSD` — BTC / USD
- `MIL-TNO` — ETF/ EUR  
- `LSE-XS8R` — ETF/ (BGX -> GBP/100)  
- `SP500` — S&P500 index / USD

Up to you to correctly bind the currency and pass it, go to : https://github.com/fawazahmed0/exchange-api
(FREE and RELIABLE API for currrency live price)

## Define your symbols

- Use TradingView’s correct slug format:  
  `https://www.tradingview.com/symbols/{symbol}/`  
- Define your `slugs` list in the script accordingly.

## Usage

```bash
python fetch_tradingview_price.py
```

## Output Expected

```bash
https://www.tradingview.com/symbols/BTCUSD/ = 116876.0 USD
https://www.tradingview.com/symbols/MIL-TNO/ = 93.79 EUR
https://www.tradingview.com/symbols/LSE-XS8R/ = 9836.192 BGX
https://www.tradingview.com/symbols/SP500/ = 6346.58 index cash USD

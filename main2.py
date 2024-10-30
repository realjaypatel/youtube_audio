from flask import Flask, request, render_template
import yt_dlp
import yfinance as yahooFinance

app = Flask(__name__)

# Home page with search form
@app.route('/')
def index():
    return render_template('index.html')


@app.get("/api/<ticker>")
def read_root(ticker):
    stockdata = yahooFinance.Ticker(ticker)
    stockdata = stockdata.info
    return {"data": stockdata}

@app.get("/ticker/<ticker>")
def read_ticker(ticker):
    stockdata = yahooFinance.Ticker(ticker)
    stockdata = stockdata.info
    return {"data": stockdata}

if __name__ == '__main__':
    app.run(debug=True)

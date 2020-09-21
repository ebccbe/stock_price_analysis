from flask import Flask, render_template, request, current_app
from stock import stock_info as stk, table_info as ttk, schart as sch, boxplot as box

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/stockpml/')
def stockpml():
    return render_template("stockpml.html")

@app.route("/predict", methods=["POST"])
def predict():
    output = request.form['stock_n']
    infoutput = stk(str(output))
    ticker = infoutput[0]
    company = infoutput[1]
    city = infoutput[2]
    country = infoutput[3]
    currency = infoutput[4]
    stockex = infoutput[5]
    website = infoutput[6]
    dhigh = infoutput[7]
    dlow = infoutput[8]
    taboutput = ttk(str(output))
    schart = sch(str(output))
    boxchart = box(str(output))
    # candlec = cad(str(output))
    return render_template('stockpml.html',  ticker_txt='Ticker: {}'.format(ticker), company_txt='Company : {}'.format(company),
                           city_txt='City : {}'.format(city), country_txt='Country : {}'.format(country),
                           currency_txt='Currency : {}'.format(currency),
                           se_txt='Stock Exchange : {}'.format(stockex), web_txt='Website : {}'.format(website),
                           dh_txt='Day High : {}'.format(dhigh), dl_txt='Day Low : {}'.format(dlow),
                           tables=taboutput.to_html(classes='data', header=True, index=False), plot=schart, plot2=boxchart)


if __name__ == "__main__":
    app.run(debug=True)

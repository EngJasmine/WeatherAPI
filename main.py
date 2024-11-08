from flask import Flask, render_template
import pandas as pd


app=Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")


''''@app.route("/api/v1/<word>")
def about(word):
    definition=word.upper()
    result={'word':word,'Definition':definition}
    return result'''
@app.route("/api/v1/<station>/<date>")
def api(station,date):
    filname='data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df=pd.read_csv(filname,skiprows=20, parse_dates=['    DATE'])
    temperature=df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    print(station)
    print(filname)
    result_dict={'Station':station,
                 'Date':date,
                 'Temperature':temperature}
    return result_dict


if __name__==('__main__'):
    app.run(debug=True)
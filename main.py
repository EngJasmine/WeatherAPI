from flask import Flask, render_template
import pandas as pd


app=Flask("Website")

variable=pd.read_csv('data_small/stations.txt',skiprows=17)
stations=variable[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html",data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def api(station,date):
    filname='data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df=pd.read_csv(filname,skiprows=20, parse_dates=['    DATE'])
    temperature=df.loc[df['    DATE']==date]['   TG'].squeeze()/10

    result_dict={'Station':station,
                 'Date':date,
                 'Temperature':temperature}
    return result_dict

@app.route("/api/v1/<station>")
def all_data(station):
    filname='data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df=pd.read_csv(filname,skiprows=20, parse_dates=['    DATE'])
    result_dict=df.to_dict(orient='records')
    return result_dict

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station,year):
    filname='data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df=pd.read_csv(filname,skiprows=20)
    df['    DATE']=df['    DATE'].astype(str)
    result=df[df['    DATE'].str.startswith(str(year))]
    return result.to_dict(orient='records')

if __name__==('__main__'):
    app.run(debug=True)
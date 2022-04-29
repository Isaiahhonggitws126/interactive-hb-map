from flaskr import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

@app.route("/")
def index():

    df = pd.read_json('../data/courts.json', orient='records') 
    df = df.dropna(axis=0)

    fig = px.scatter_mapbox(df, lat='lat', lon='lon', text='Name', size='Num_of_Courts')
    fig.update_layout(mapbox_style="open-street-map")

    return render_template("layout.html")
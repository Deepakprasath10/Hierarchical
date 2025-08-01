from flask import Flask, render_template, request
import pandas as pd
from model import cluster_energy_data
from utils import save_cluster_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file = request.files['file']
    clusters = int(request.form['clusters'])

    df = pd.read_csv(file)
    clustered_df = cluster_energy_data(df, clusters)
    save_cluster_plot(clustered_df)

    return render_template('result.html', tables=[clustered_df.to_html(classes='data')], img='static/cluster_plot.png')

if __name__ == "__main__":
    app.run(debug=True)

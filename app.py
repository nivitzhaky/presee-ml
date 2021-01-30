import numpy as np
import warnings
from flask import Flask, request
import os.path
warnings.filterwarnings("ignore")
from keras.models import load_model
from keras.optimizers import Adam
import h5py
import pandas as pd
import tensorflow as tf

app = Flask(__name__)
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "model.hdf5")

model = load_model(path, compile=False)
model.compile(loss='binary_crossentropy', optimizer=Adam())
global graph
graph = tf.get_default_graph()

@app.route("/",  methods=['POST'])
def index():
    f = request.files['file']
    df = pd.read_csv(f, sep="\t")
    cur = np.delete(df.values, 12, axis=1)
    cur = np.divide(cur, 1000.0)
    cur = cur[0:4096]
    cur = np.swapaxes(cur,0,1)
    cur=np.dstack((cur))
    with graph.as_default():
        res = model.predict(cur, batch_size=10, verbose=1)

    res = np.around(res, decimals=2)
    d = {'1dAVb' : res[0][0],'RBBB' : res[0][1],'LBBB' : res[0][2],
         'SB': res[0][3], 'AF': res[0][4], 'ST': res[0][5]
         }
    return str(d)
@app.route("/",  methods=['GET'])
def index2():
    return "hello"
app.run(host='0.0.0.0', port=8080)

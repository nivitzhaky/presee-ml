import numpy as np
import warnings
import argparse
from flask import Flask, render_template, session, redirect, url_for, request
import csv
import os.path
warnings.filterwarnings("ignore")
# from keras.models import load_model
# from keras.optimizers import Adam
# import tensorflow as tf
import h5py
import pandas as pd
# import tensorflow as tf

app = Flask(__name__)
# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(my_path, "model.hdf5")

# model = load_model(path, compile=False)
# model.compile(loss='binary_crossentropy', optimizer=Adam())
# global graph
# graph = tf.get_default_graph()

@app.route("/",  methods=['POST'])
def index():
    # f = request.files['file']
    # df = pd.read_csv(f, sep="\t")
    # cur = np.delete(df.values, 12, axis=1)
    # cur = np.divide(cur, 1000.0)
    # cur = cur[0:4096]
    # cur = np.swapaxes(cur,0,1)
    # cur=np.dstack((cur))
    # with graph.as_default():
    #     y_score = model.predict(cur, batch_size=10, verbose=1)
    # return str(y_score)
    return ""

app.run(host='0.0.0.0', port=8080)

from flask import Flask
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from common import threading_func_wrapper
import json
#%%
def dump():
    from CONSTANT import OUTPUT_PICKLE_FILENAME
    import pickle
    with open(OUTPUT_PICKLE_FILENAME, "rb") as file:
        history = pickle.load(file)
    last = history[-1]['time']
    print(len(history), last['time'])

dump()

#%%


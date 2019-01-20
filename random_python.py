import sys, os
from flask import Flask, render_template
from flask import request
import glob
import re
import json

app = Flask(__name__)

zen_python = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!"
]

@app.route('/', methods=['GET', 'POST'])
def random_python():
    global zen_python

    import random
    import time
    random.seed(time.time())

    random_number = random.randint(1, len(zen_python))-1
    return render_template('zen_python.html', zen_python=zen_python[random_number])

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0')
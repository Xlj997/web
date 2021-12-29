#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 11:51
# @Author  : lj
# @File    : main.py
from flask import Flask

app = Flask(__name__)
@app.route('/',methods=['GET'])
def healthz():
    return {
        'code': 200,
        'data': None
    }
if __name__ == '__main__':
    app.run(host='0.0.0.0')
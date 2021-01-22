"""
author:gbs
c_date:2021/1/22 10:06
u_date:2021/1/22 10:06
reversion:1.0
file_name:demo2
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "你好你好"\

@app.route('/<int:pk>')
def detail(pk):
    return f"欢迎{pk}"


if __name__ == '__main__':
    app.run(host='192.168.11.14',port=6900,debug=True)


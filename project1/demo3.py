"""
author:gbs
c_date:2021/1/22 10:31
u_date:2021/1/22 10:31
reversion:1.0
file_name:demo3
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    name="陈乐"
    # sex ="女"
    return render_template("index1.html",**locals())

if __name__ == '__main__':
    app.run(debug=True)


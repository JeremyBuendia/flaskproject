"""
author:gbs
c_date:2021/1/22 11:37
u_date:2021/1/22 11:37
reversion:1.0
file_name:demo4
"""
from flask import Flask, render_template, request, redirect, session, url_for,flash
import os

from views.main import mainbp
from views.user import userbp
app = Flask(__name__)
app.register_blueprint(mainbp)
app.register_blueprint(userbp)

app.secret_key = os.urandom(24)






if __name__ == '__main__':
    app.run(debug=True)

"""
author:gbs
c_date:2021/1/23 14:08
u_date:2021/1/23 14:08
reversion:1.0
file_name:user
"""

from flask import Flask, render_template, request, redirect, session, url_for,flash,Blueprint

userbp=Blueprint("user",__name__)
users = [
    {
        "email": "11@qq.com",
        "password": "1",
    },
]
@userbp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html', **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                session["user"] = email
                return redirect(url_for("main.index"))
            else:
                flash("邮箱或密码错误！")
        return redirect(url_for("user.login"))


@userbp.route('/regist',methods=["GET","POST"])
def regist():
    if request.method == "GET":
        return render_template('regist.html', **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        for u in users:
            if email==u["email"]:
                flash("邮箱已存在！")
                return redirect(url_for("user.regist"))
            elif password !=password2:
                flash("两次密码输入不一致！")
                return redirect(url_for("user.regist"))
            else:
                users.append({
                    "email": email,
                    "password": password,
                },)
                return redirect(url_for("user.login"))





@userbp.route('/logout')
def logout():
    session.pop("user")
    return redirect(url_for("index"))


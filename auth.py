"""
Authentication — session-based, single password (no username).
Matches the auth model used in the clips and class-plans dashboards.
"""
import os
from functools import wraps
from flask import Blueprint, session, redirect, url_for, render_template, request

auth_bp = Blueprint("auth", __name__)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password", "")
        if os.getenv("DASHBOARD_PASS") and password == os.getenv("DASHBOARD_PASS"):
            session["logged_in"] = True
            return redirect(url_for("index"))
        return render_template("login.html", error="Invalid password")
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("auth.login"))

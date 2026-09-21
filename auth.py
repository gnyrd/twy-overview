"""
Authentication — session-based, password only (no username).
Matches the auth model used in the clips and class-plans dashboards.
Two passwords open the same session: DASHBOARD_PASS (Tiff's) and ADMIN_PASS
(JP's, the kill switch canary of 2026-09-21). Nothing records which one was used.
"""
import os
from functools import wraps
from flask import Blueprint, session, redirect, url_for, render_template, request
from twy_platform import device_id

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
        accepted = [p for p in (os.getenv("DASHBOARD_PASS"), os.getenv("ADMIN_PASS")) if p]
        if password in accepted:
            session["logged_in"] = True
            device_id.record("login", {"pw": "admin" if password == os.getenv("ADMIN_PASS") else "dashboard"})
            return redirect(url_for("index"))
        return render_template("login.html", error="Invalid password")
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("auth.login"))

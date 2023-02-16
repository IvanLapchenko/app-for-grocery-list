from flask import render_template, request, session
from grocery_list import app, db_controls


@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["shopping_items"] = db_controls.get_db()
    return render_template("index.html",
                           all_items=session["all_items"],
                           shopping_items=session["shopping_items"])


@app.route("/remove_items", methods=["POST", "GET"])
def remove_items():
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            session.modified = True
    return render_template("index.html",
                           all_items=session["all_items"],
                           shopping_items=session["shopping_items"])


@app.route("/add_items", methods=["POST"])
def add_items():
    session["shopping_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html",
                           all_items=session["all_items"],
                           shopping_items=session["shopping_items"])

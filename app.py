from flask import Flask, redirect, request, url_for, jsonify
import sqlite3
import json

app = Flask(__name__)
server = f"src/mydatabase.db"


def get_db_connection():
    conn = sqlite3.connect(server)
    return conn


@app.route("/")
def index():
    return '<p>Hello World!!!</p>'


@app.route("/address", methods=["POST", "GET"])
def address():
    conn = get_db_connection()
    if request.method == "GET":
        addresses = conn.execute("""
            SELECT * FROM address
        """).fetchall()
        conn.close()
        return addresses
    if request.method == "POST":
        street_no = request.form["street_no"]
        address_line_1 = request.form["address_line_1"]
        address_line_2 = request.form["address_line_2"]
        postal_code = request.form["postal_code"]
        city = request.form["city"]
        province = request.form["province"]

        conn.execute("""
            INSERT INTO address VALUES (?, ?, ?, ?, ?, ?)
        """, (street_no, address_line_1, address_line_2, postal_code, city, province))
        conn.commit()
        conn.close()
        return request.form


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect, request, url_for
import sqlite3

app = Flask(__name__)
server = f"src/mydatabase.db"


def get_db_connection():
    conn = sqlite3.connect(server)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def hello_world():
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
    return


if __name__ == '__main__':
    app.run(debug=True, port=8080)

import sqlite3


con = sqlite3.connect(f"mydatabase.db")
cur = con.cursor()

# cur.execute("""
#     CREATE TABLE address (
#         street_no integer,
#         address_line_1 text,
#         address_line_2 text,
#         postal_code text,
#         city text,
#         province text
#     )
# """)

data = [
    (24, "Greenfield Ave", "Apt 3406", "M2N0L1", "Toronto", "Ontario"),
    (25, "Bluefield Ave", "Apt 1102", "M2N0L2", "Toronto", "Ontario"),
    (26, "Redfield Ave", "Apt 2598", "M2N0L3", "Toronto", "Ontario"),
]

cur.executemany("""
    INSERT INTO address VALUES (?, ?, ?, ?, ?, ?)
""", data)

con.commit()

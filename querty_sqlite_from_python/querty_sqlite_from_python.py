import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# query = "select * from recent_grads;"
# cursor.execute(query)
# results = cursor.fetchall()
# print(results[0:2])

# query = """
# SELECT major
# FROM recent_grads;
# """
# cursor.execute(query)
# majors = cursor.fetchall()
# print(majors[0:3])

first_result = cursor.fetchone()
second_result = cursor.fetchone()
next_five_results = cursor.fetchmany(5)

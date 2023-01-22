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
# # print(majors[0:3])

# query = """
# SELECT
#     Major,
#     Major_category
# FROM recent_grads;
# """
# cursor.execute(query)
# five_results = cursor.fetchmany(5)
# print(five_results)

# query = """
# SELECT
#     Major
# FROM recent_grads
# ORDER BY Major DESC
# """
# cursor.execute(query)
# reverse_alphabetical = cursor.fetchall()
# print(reverse_alphabetical[0:5])
# conn.close()

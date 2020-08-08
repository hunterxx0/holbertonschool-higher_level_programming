#!/usr/bin/python3
"""
Lists all cities from the database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id\
 = cities.state_id WHERE states.name = %s ORDER BY cities.id", (argv[4], ))
    query_rows = cur.fetchall()
    ss = ""
    for row in query_rows:
        ss += row[0]
        if row[0] not in query_rows[len(query_rows)-1]:
            ss += ', '
    print(ss)
    cur.close()
    conn.close()

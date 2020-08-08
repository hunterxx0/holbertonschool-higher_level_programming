#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = '{}' ORDER BY \
states.id".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print("{}".format(row))
    cur.close()
    conn.close()

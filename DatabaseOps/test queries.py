"""test file for running sql queries"""
import InputObjects

import sqlite3

con = sqlite3.connect("birding.db")

cur = con.cursor()

def get_last_row_id():
    test_exp = InputObjects.expedition("test","test",[],cur)
    test_exp.to_database()
    res = cur.execute("select last_insert_rowid()")
    print(res.fetchone()[0])

def print_all_expedition_birds():
    for row in cur.execute("select * from expedition_bird"):
        print(row)

    con.commit()
#print_all_expedition_birds()

def generate_bird_list():
    birdlist = []
    for row in cur.execute("select name from bird"):
        birdlist.append(row[0])
    print(birdlist)
generate_bird_list()
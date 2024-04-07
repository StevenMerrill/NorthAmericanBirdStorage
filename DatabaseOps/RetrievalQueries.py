import sqlite3

def generate_bird_list():
    con = sqlite3.connect('birding.db')
    cur = con.cursor()
    birdlist = []
    for row in cur.execute("select name from bird"):
        birdlist.append(row[0])
    con.close()
    return (birdlist)
from InputObjects import *
import sqlite3
import csv

con = sqlite3.Connection('birding.db')

cur = con.cursor()

with open('DatabaseOps\\NACC_list_species.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for birdlist in reader:
        i_bird = bird(*birdlist,cur)
        i_bird.to_database()
        con.commit()

con.close()
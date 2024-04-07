"""Creates the "birding.db file and fills it with the tables bird, expedition_bird, and expedition"""
import sqlite3

con = sqlite3.connect('birding.db')

cur = con.cursor()

cur.execute("DROP TABLE bird")
cur.execute("DROP TABLE expedition_bird")
cur.execute("DROP TABLE expedition")


cur.execute("""CREATE TABLE bird(id int,
                                rank varchar(255),
                                name varchar(255),
                                french_name varchar(255),
                                bio_order varchar(255),
                                family varchar(255),
                                subfamily varchar(255),
                                genus varchar(255),
                                species varchar(255),
                                annotation varchar(255),
                                status_accidental bool,
                                status_hawaiian bool,
                                status_introduced bool,
                                status_nonbreeding bool,
                                status_extinct bool,
                                status_misplaced bool)""")

cur.execute("""CREATE TABLE expedition_bird(ID integer primary key autoincrement,
                                            bird_ID int,
                                            exp_ID int,
                                            pic varchar(255),
                                            type varchar(255),
                                            number int)""")

cur.execute("""CREATE TABLE expedition(ID integer primary key autoincrement,
                                        place varchar(255),
                                        date int)""")

con.commit()

con.close()
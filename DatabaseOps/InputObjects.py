#InputObjects.py
"""contains object structure for objects That The user creates when going on an expedition"""

import sqlite3

class queryobject:
    def __init__(self,cursor:sqlite3.Cursor):
        self.cursor = cursor
        self.data_tuple = ()
        self.table = ''
        self.tablekey = ""

    def to_database(self):
        self.cursor.execute(f'INSERT INTO {self.table} {self.tablekey} Values{self.data_tuple}')

    def print_db_string(self):
        print(f'INSERT INTO {self.table} {self.tablekey} Values{self.data_tuple}')

class bird(queryobject):
    def __init__(self,BIRDID,rank,name,french_name,bio_order,family,subfamily,genus,species,annotation,status_accidental,status_hawaiian,status_introduced,status_nonbreeding,status_extinct,status_misplaced,cursor):
        super().__init__(cursor)
        self.BIRDID = BIRDID
        self.rank = rank
        self.name = name
        self.french_name = french_name
        self.bio_order = bio_order
        self.family = family
        self.subfamily = subfamily
        self.genus = genus
        self.species = species
        self.annotation = annotation
        self.status_accidental = bool(status_accidental)
        self.status_hawaiian = bool(status_hawaiian)
        self.status_introduced = bool(status_introduced)
        self.status_nonbreeding = bool(status_nonbreeding)
        self.status_extinct = bool(status_extinct)
        self.status_misplaced = bool(status_misplaced)
        self.data_tuple = (BIRDID,rank,name,french_name,bio_order,family,subfamily,genus,species,annotation,status_accidental,status_hawaiian,status_introduced,status_nonbreeding,status_extinct,status_misplaced)
        self.table = 'bird'
        self.tablekey = '(ID,rank,name,french_name,bio_order,family,subfamily,genus,species,annotation,status_accidental,status_hawaiian,status_introduced,status_nonbreeding,status_extinct,status_misplaced)'


class expedition_bird(queryobject):
    def __init__(self,BIRDID,EXPID,PIC,SPECIES,NUM_SEEN,cursor):
        super().__init__(cursor)
        self.BIRDID = BIRDID
        self.EXPID = EXPID
        self.PIC=PIC
        self.SPECIES = SPECIES
        self.NUM_SEEN = NUM_SEEN
        self.data_tuple = (BIRDID,EXPID,PIC,SPECIES,NUM_SEEN)
        self.table = 'expedition_bird'
        self.tablekey = '(BIRD_ID,EXP_ID,PIC,TYPE,NUMBER)'

class expedition(queryobject):
    def __init__(self,PLACE,DATE,BIRDS,cursor):
        super().__init__(cursor)
        self.PLACE = PLACE
        self.DATE = DATE
        self.BIRDS = BIRDS
        self.data_tuple = (PLACE,DATE)
        self.table = 'expedition'
        self.tablekey = '(PLACE,DATE)'

    def birds_to_database(self):
        for bird in self.BIRDS:
            bird.to_database()

    
    
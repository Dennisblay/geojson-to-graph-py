from database.db import Database

db = Database(dbname='routes', user='postgres', host='localhost')
db.connect()
db.execute_query('insert into nodes (name, point_geom)  values ( %s, st_geomfromtext( %s ))',
                 ('n1', 'POINT( -22343.3343, 43432.343234)'))
db.close()

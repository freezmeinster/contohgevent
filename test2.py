import gevent.monkey
import time

from psycopg2.pool import ThreadedConnectionPool

gevent.monkey.patch_all()

db = ThreadedConnectionPool(1,10, 
		database="getest",
               	user="bram",
                password="bram",
                host="localhost",
                port=5432)

con = db.getconn()
cur = con.cursor()

def runme(id):
    print "Starting ID %s" % id
    query = "insert into test values (%s)" % id
    cur.execute(query)
    con.commit()
    print "ID %s Done" % id

jobs = [gevent.spawn(runme, _id) for _id in range(1000)]

gevent.wait(jobs)

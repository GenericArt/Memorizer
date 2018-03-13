import sqlite3




		
def create_table(db, tableName, columns):

	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("CREATE TABLE %s (%s)" % (tableName, columns))




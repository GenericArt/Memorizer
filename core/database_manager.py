import sqlite3
from pprint import pprint
from random import choice


def getNumberOfRows(db, tableName):
	
	con = sqlite3.connect(db)
	
	result = []

	with con:

		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("SELECT row_id FROM %s" % (tableName))

		rows = cur.fetchall()
		result = cur.fetchall()
		for row in rows:
			result.append(row[0])
	con.close()
	return result



def getRowById(db, tableName, rowID):

	con = sqlite3.connect(db)
	rowDict = {}

	with con:

		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("SELECT * FROM %s WHERE row_id = %s" % (tableName, rowID))
		rows = cur.fetchall()

		for row in rows:
			for key in row.keys():
				print(key, row[key])
				rowDict[key] = row[key]
			

	con.close()

	return rowDict



def getDecoyWords(db):

	con = sqlite3.connect(db)
	words = []

	with con:

		con.row_factory = sqlite3.Row
		cur = con.cursor()

		cur.execute("SELECT * FROM DecoyWords")

		rows = cur.fetchall()
		row = choice(rows)
		
		words = (row["wordsets"].split("-"))

		
	con.close()

	return words



def getARow(db, tableName, rowID):

	con = sqlite3.connect(db)
	data = {}

	with con:

		con.row_factory = sqlite3.Row
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE row_id=%s" % (tableName, rowID))

		rows = cur.fetchall()
		for key in rows[0].keys():
			data[key] = rows[0][key]

		
	con.close()

	return data
 






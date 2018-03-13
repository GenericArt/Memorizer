import sqlite3, json
from pprint import pprint



def setup():
	

	conn = sqlite3.connect('core/main.db')
	cur = conn.cursor()
	

	tableName = "DefaultVerseList"
	columns = "verseID text, verse text, answer text, verseType text"

	cur.execute("CREATE TABLE %s (%s)" % (tableName, columns))
	


	data = json.load(open('core/default_verse_db_build.json', encoding='utf-8'))
	

	for verse in data.keys():
		cd = data[verse]
		row = tuple((cd["verseID"], cd["verse"], cd["answer"], cd["verseType"]))
		print(row)

		cur.execute("INSERT INTO DefaultVerseList VALUES (?,?,?,?)", row)


	conn.commit()
	conn.close()


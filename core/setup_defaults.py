import sqlite3, json, csv
from pprint import pprint



def setup():
	
	

	conn = sqlite3.connect('core/main.db')
	cur = conn.cursor()
	

	### Setup Verses Table

	tableName = ["DefaultEnglish", "DefaultKorean"]
	columns = "name_id INTEGER PRIMARY KEY AUTOINCREMENT, verseID text, verse text, answer1 text, answer2 text, answer3 text, verseType text"

	for lang in tableName:
		cur.execute("CREATE TABLE %s (%s)" % (lang, columns))
	


	data = json.load(open('core/default_verse_db_build.json', encoding='utf-8'))
	conn.commit()

	for verse in data.keys():
		verType = data[verse]["verseType"]
		scriptEng = data[verse]["scripture"]["english"]
		scriptKor = data[verse]["scripture"]["korean"]

		rowEng = tuple((scriptEng["verseID"], scriptEng["verse"], scriptEng["answer1"], scriptEng["answer2"], scriptEng["answer3"], verType))
		rowKor = tuple((scriptKor["verseID"], scriptKor["verse"], scriptKor["answer1"], scriptEng["answer2"], scriptEng["answer3"], verType))

		cur.execute("INSERT INTO DefaultEnglish VALUES (NULL,?,?,?,?,?,?)", rowEng)
		cur.execute("INSERT INTO DefaultKorean VALUES (NULL,?,?,?,?,?,?)", rowKor)



	conn.commit()
	### Setup Decoy Table

	decoyWordsFilePath = "core/decoy_words.csv"

	cur.execute("CREATE TABLE DecoyWords (name_id INTEGER PRIMARY KEY AUTOINCREMENT, wordsets text)")
	conn.commit()
	listOfListDecoys = []
	with open(decoyWordsFilePath) as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)
			listOfListDecoys.append((str("-".join(row))))
	
	for wordset in listOfListDecoys:
		print(wordset)
		print("---------")
		cur.execute("INSERT INTO DecoyWords VALUES (NULL,?)", (wordset,))



	conn.commit()
	conn.close()


import sqlite3, json, csv



def setup():



    conn = sqlite3.connect('core/main.db')
    cur = conn.cursor()


    ### Setup Verses Table

    tableName = ["DefaultEnglish", "DefaultKorean"]
    columns = "row_id INTEGER PRIMARY KEY AUTOINCREMENT, verseID text, verse text, verseQuest text, answer1 text, answer2 text, answer3 text, verseType text"

    for lang in tableName:
        cur.execute("CREATE TABLE %s (%s)" % (lang, columns))



    data = json.load(open('core/default_verse_db_build.json', encoding='utf-8'))
    conn.commit()

    for verse in data.keys():
        verType = data[verse]["verseType"]
        scriptEng = data[verse]["scripture"]["english"]
        scriptKor = data[verse]["scripture"]["korean"]

        rowEng = tuple((scriptEng["verseID"], scriptEng["verse"], scriptEng["verseQuest"], scriptEng["answer1"], scriptEng["answer2"], scriptEng["answer3"], verType))
        rowKor = tuple((scriptKor["verseID"], scriptKor["verse"], scriptEng["verseQuest"], scriptKor["answer1"], scriptEng["answer2"], scriptEng["answer3"], verType))

        cur.execute("INSERT INTO DefaultEnglish VALUES (NULL,?,?,?,?,?,?,?)", rowEng)
        cur.execute("INSERT INTO DefaultKorean VALUES (NULL,?,?,?,?,?,?,?)", rowKor)



    conn.commit()
    ### Setup Decoy Table

    decoyWordsFilePath = "core/decoy_words.csv"

    cur.execute("CREATE TABLE DecoyWords (row_id INTEGER PRIMARY KEY AUTOINCREMENT, wordsets text)")
    conn.commit()
    listOfListDecoys = []
    with open(decoyWordsFilePath) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            listOfListDecoys.append((str("-".join(row))))

    for wordset in listOfListDecoys:
        cur.execute("INSERT INTO DecoyWords VALUES (NULL,?)", (wordset,))



    conn.commit()

    # Setup Quiz Questions Table
    quizQuestionsJSon = json.load(open('core/quizquestions.json'))

    cur.execute("CREATE TABLE QuizQuestions (row_id INTEGER PRIMARY KEY AUTOINCREMENT, difficulty text, question text, answer text, decoyone text, decoytwo text, decoythree text)")
    conn.commit()

    for q in quizQuestionsJSon:
        qRow = tuple((q["category"], q["question"], q["answer"], q["decoyOne"], q["decoyTwo"], q["decoyThree"]))
        cur.execute("INSERT INTO QuizQuestions VALUES (NULL,?,?,?,?,?,?)", qRow)

    conn.commit()

    # Setup Mood Verses Table
    moodVersesJSon = json.load(open('core/moodverses.json'))

    cur.execute("CREATE TABLE MoodVerses (row_id INTEGER PRIMARY KEY AUTOINCREMENT, category text, passage text, verse text)")
    conn.commit()

    for mood in moodVersesJSon:
        moodRow = tuple((mood['category'], mood['passage'], mood['verse']))
        cur.execute("INSERT INTO MoodVerses VALUES (NULL,?,?,?)", moodRow)

    conn.commit()
    conn.close()

